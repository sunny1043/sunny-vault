#!/usr/bin/env python3
"""
导入 Claude Desktop local-agent-mode 会话到 Markdown。

仅扫描本地文件：
  ~/Library/Application Support/Claude/local-agent-mode-sessions/

输出三种模式：
  index  - 会话索引（标题、时间、消息数、首问）
  digest - 每会话保留首问、末问、以及助手回复摘要（默认）
  full   - 完整转录（可能很大，建议配合筛选）
"""

from __future__ import annotations

import argparse
import json
import re
import sys
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable

# macOS 上 Claude Desktop 的 local-agent-mode 数据根目录
DEFAULT_CLAUDE_DIR = Path.home() / "Library/Application Support/Claude/local-agent-mode-sessions"


def ts_to_iso(ms: int | None) -> str:
    """把毫秒时间戳转为本地可读 ISO 格式。"""
    if ms is None:
        return ""
    return datetime.fromtimestamp(ms / 1000, tz=timezone.utc).astimezone().isoformat(timespec="minutes")


def find_session_dirs(root: Path) -> Iterable[Path]:
    """递归查找所有 local_<uuid>.json 所在的会话目录。"""
    if not root.exists():
        return
    yield from root.rglob("local_*.json")


def find_output_jsonl(session_dir: Path, cli_session_id: str) -> Path | None:
    """在会话目录下按 cliSessionId 找对应的 .jsonl 对话文件。"""
    for candidate in session_dir.rglob(f"{cli_session_id}.jsonl"):
        if candidate.is_file():
            return candidate
    return None


def extract_messages(jsonl_path: Path) -> list[dict]:
    """
    从 .jsonl 文件中提取用户与助手的文本消息。
    返回 [{"role": "user"|"assistant", "content": str, "timestamp": str}, ...]
    """
    messages: list[dict] = []
    with jsonl_path.open("r", encoding="utf-8", errors="replace") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            try:
                event = json.loads(line)
            except json.JSONDecodeError:
                continue

            event_type = event.get("type")
            ts = event.get("timestamp", "")

            if event_type == "user":
                content = event.get("message", {}).get("content", "")
                if content:
                    messages.append({"role": "user", "content": str(content), "timestamp": ts})

            elif event_type == "assistant":
                msg = event.get("message", {})
                texts: list[str] = []
                for block in msg.get("content", []) or []:
                    if isinstance(block, dict) and block.get("type") == "text":
                        text = block.get("text", "")
                        if text:
                            texts.append(text)
                if texts:
                    messages.append({"role": "assistant", "content": "\n".join(texts), "timestamp": ts})

    return messages


def load_session(meta_path: Path) -> dict | None:
    """读取会话元数据，找不到对话文件时返回 None。"""
    try:
        with meta_path.open("r", encoding="utf-8") as f:
            meta = json.load(f)
    except (json.JSONDecodeError, OSError):
        return None

    cli_session_id = meta.get("cliSessionId")
    if not cli_session_id:
        return None

    session_dir = meta_path.parent
    jsonl_path = find_output_jsonl(session_dir, cli_session_id)
    if not jsonl_path:
        return None

    messages = extract_messages(jsonl_path)
    if not messages:
        return None

    created = meta.get("createdAt")
    last = meta.get("lastActivityAt")

    return {
        "session_id": meta.get("sessionId", meta_path.stem),
        "cli_session_id": cli_session_id,
        "title": meta.get("title") or "未命名会话",
        "initial_message": meta.get("initialMessage", ""),
        "model": meta.get("model", ""),
        "created_at": created,
        "last_activity_at": last,
        "created_iso": ts_to_iso(created),
        "last_iso": ts_to_iso(last),
        "message_count": len(messages),
        "user_message_count": sum(1 for m in messages if m["role"] == "user"),
        "messages": messages,
        "meta_path": meta_path,
        "jsonl_path": jsonl_path,
    }


def passes_filters(session: dict, since: datetime | None, until: datetime | None, keyword: str | None) -> bool:
    """按时间、关键词过滤会话。"""
    created = session.get("created_at")
    if created is not None:
        created_dt = datetime.fromtimestamp(created / 1000, tz=timezone.utc)
        if since and created_dt < since:
            return False
        if until and created_dt > until:
            return False

    if keyword:
        keyword_lower = keyword.lower()
        haystack = " ".join([
            session.get("title", ""),
            session.get("initial_message", ""),
            *(m["content"] for m in session.get("messages", [])),
        ]).lower()
        if keyword_lower not in haystack:
            return False

    return True


def truncate_text(text: str, max_chars: int, suffix: str = "\n\n…（已截断）") -> str:
    """截断文本并追加提示。"""
    if max_chars <= 0 or len(text) <= max_chars:
        return text
    # 在句子或段落边界截断，避免断词
    cut = text[:max_chars]
    last_period = max(cut.rfind("。"), cut.rfind("."), cut.rfind("\n"))
    if last_period > max_chars * 0.8:
        cut = cut[: last_period + 1]
    return cut.rstrip() + suffix


def format_messages_full(messages: list[dict]) -> str:
    """完整转录消息。"""
    lines: list[str] = []
    for m in messages:
        role_label = "👤 用户" if m["role"] == "user" else "🤖 助手"
        lines.append(f"**{role_label}** ({m.get('timestamp', '')}):")
        lines.append("")
        lines.append(m["content"])
        lines.append("")
    return "\n".join(lines)


def clean_user_content(content: str) -> str:
    """去掉 <uploaded_files>、图片 base64、工具结果 JSON 等噪音，仅保留可读问题。"""
    # 去掉文件上传 XML
    content = re.sub(r"<uploaded_files>.*?</uploaded_files>", "", content, flags=re.DOTALL)
    content = re.sub(r"<file>.*?</file>", "", content, flags=re.DOTALL)
    # 去掉图片内容（Claude JSONL 中图片以 [{'type': 'image', 'source': {'type': 'base64', ...}}] 形式出现）
    if "'type': 'image'" in content or '"type": "image"' in content:
        return "[图片]"
    # 去掉纯工具结果（形如 [{'tool_use_id': ...}]
    if content.strip().startswith("[{") and "'tool_use_id'" in content:
        return "[工具结果]"
    return content.strip()


def format_messages_digest(messages: list[dict], max_user_chars: int = 200, max_assistant_chars: int = 400, initial_message: str = "") -> str:
    """
    生成高度紧凑的摘要，适合一次性注入大量会话上下文：
      - 首条用户问题（截断；若首条是图片/工具结果，回退到 metadata 中的 initialMessage）
      - 首条助手回复（截断）
      - 若会话很短（<=2 条消息），直接给出完整内容
    """
    lines: list[str] = []
    user_messages = [m for m in messages if m["role"] == "user"]
    assistant_messages = [m for m in messages if m["role"] == "assistant"]
    short_conversation = len(messages) <= 2

    if short_conversation:
        return format_messages_full(messages)

    if user_messages:
        first_prompt = clean_user_content(user_messages[0]["content"])
        if (not first_prompt or first_prompt.startswith("[")) and initial_message:
            first_prompt = clean_user_content(initial_message)
        if first_prompt:
            lines.append(f"**首问**: {truncate_text(first_prompt, max_user_chars, suffix=' …')}")

    if assistant_messages:
        lines.append(f"**首答**:")
        lines.append(truncate_text(assistant_messages[0]["content"], max_assistant_chars))
        lines.append("")

    return "\n".join(lines)


def render_index(sessions: list[dict]) -> str:
    """渲染索引模式 Markdown。"""
    lines = [
        "---",
        "来源: Claude Desktop local-agent-mode 会话",
        f"导出日期: {datetime.now().isoformat(timespec='minutes')}",
        f"会话数: {len(sessions)}",
        "模式: index",
        "---",
        "",
        "# Claude 历史会话索引",
        "",
    ]

    for i, s in enumerate(sessions, 1):
        lines.append(f"## {i}. {s['title']}")
        lines.append(f"- **会话 ID**: `{s['session_id']}`")
        lines.append(f"- **创建时间**: {s['created_iso']}")
        lines.append(f"- **最后活跃**: {s['last_iso']}")
        lines.append(f"- **模型**: {s['model']}")
        lines.append(f"- **消息数**: {s['message_count']}（用户 {s['user_message_count']} / 助手 {s['message_count'] - s['user_message_count']}）")
        lines.append(f"- **首问**: {s['initial_message'] or s['messages'][0]['content']}")
        lines.append("")

    return "\n".join(lines)


def render_digest(sessions: list[dict], max_user_chars: int = 200, max_assistant_chars: int = 400) -> str:
    """渲染摘要模式 Markdown。"""
    lines = [
        "---",
        "来源: Claude Desktop local-agent-mode 会话",
        f"导出日期: {datetime.now().isoformat(timespec='minutes')}",
        f"会话数: {len(sessions)}",
        "模式: digest",
        "说明: 仅保留每个会话的首问与首答摘要，如需完整内容请用 --mode full 对指定会话导出。",
        "---",
        "",
        "# Claude 历史会话摘要",
        "",
        "> 以下是从 Claude Desktop 本地导出的历史会话摘要，可作为当前对话的上下文参考。",
        "",
    ]

    for i, s in enumerate(sessions, 1):
        lines.append(f"## {i}. {s['title']}")
        lines.append(f"- 时间: {s['created_iso']} ~ {s['last_iso']}")
        lines.append(f"- 模型: {s['model']}")
        lines.append(f"- 消息: {s['message_count']} 条")
        lines.append("")
        lines.append(format_messages_digest(s["messages"], max_user_chars, max_assistant_chars, s.get("initial_message", "")))
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def render_full(sessions: list[dict]) -> str:
    """渲染完整模式 Markdown。"""
    lines = [
        "---",
        "来源: Claude Desktop local-agent-mode 会话",
        f"导出日期: {datetime.now().isoformat(timespec='minutes')}",
        f"会话数: {len(sessions)}",
        "模式: full",
        "---",
        "",
        "# Claude 历史会话完整转录",
        "",
    ]

    for i, s in enumerate(sessions, 1):
        lines.append(f"## {i}. {s['title']}")
        lines.append(f"- 时间: {s['created_iso']} ~ {s['last_iso']}")
        lines.append(f"- 模型: {s['model']}")
        lines.append(f"- 消息: {s['message_count']} 条")
        lines.append(f"- 元数据: `{s['meta_path']}`")
        lines.append(f"- 对话文件: `{s['jsonl_path']}`")
        lines.append("")
        lines.append(format_messages_full(s["messages"]))
        lines.append("---")
        lines.append("")

    return "\n".join(lines)


def parse_date(value: str) -> datetime:
    """解析 YYYY-MM-DD 为 UTC 当天开始。"""
    return datetime.strptime(value, "%Y-%m-%d").replace(tzinfo=timezone.utc)


def main() -> int:
    parser = argparse.ArgumentParser(
        description="将 Claude Desktop local-agent-mode 会话导出为 Markdown。",
    )
    parser.add_argument(
        "--claude-dir",
        type=Path,
        default=DEFAULT_CLAUDE_DIR,
        help="Claude local-agent-mode-sessions 目录路径",
    )
    parser.add_argument(
        "--mode",
        choices=["index", "digest", "full"],
        default="digest",
        help="输出模式：index=索引，digest=摘要（默认），full=完整转录",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=Path("claude_sessions_context.md"),
        help="输出 Markdown 文件路径",
    )
    parser.add_argument(
        "--since",
        type=parse_date,
        help="只导出该日期之后的会话（格式 YYYY-MM-DD）",
    )
    parser.add_argument(
        "--until",
        type=parse_date,
        help="只导出该日期之前的会话（格式 YYYY-MM-DD）",
    )
    parser.add_argument(
        "--keyword",
        "-k",
        type=str,
        help="按标题或内容关键词过滤（不区分大小写）",
    )
    parser.add_argument(
        "--max-user-chars",
        type=int,
        default=200,
        help="digest 模式下首问保留的最大字符数（默认 200）",
    )
    parser.add_argument(
        "--max-assistant-chars",
        type=int,
        default=400,
        help="digest 模式下首答保留的最大字符数（默认 400）",
    )
    parser.add_argument(
        "--limit",
        type=int,
        default=0,
        help="最多导出 N 个会话（0 表示不限制）",
    )

    args = parser.parse_args()

    sessions: list[dict] = []
    for meta_path in find_session_dirs(args.claude_dir):
        session = load_session(meta_path)
        if not session:
            continue
        if passes_filters(session, args.since, args.until, args.keyword):
            sessions.append(session)

    # 默认按创建时间倒序，最近的在最前
    sessions.sort(key=lambda s: s.get("created_at") or 0, reverse=True)

    if args.limit > 0:
        sessions = sessions[: args.limit]

    if not sessions:
        print("未找到匹配的会话。", file=sys.stderr)
        return 1

    if args.mode == "index":
        md = render_index(sessions)
    elif args.mode == "digest":
        md = render_digest(sessions, args.max_user_chars, args.max_assistant_chars)
    else:
        md = render_full(sessions)

    args.output.write_text(md, encoding="utf-8")
    print(f"已导出 {len(sessions)} 个会话到: {args.output.resolve()}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
