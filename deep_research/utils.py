"""Utility functions for displaying messages and prompts in Jupyter notebooks."""

import json

from rich.console import Console
from rich.panel import Panel
from rich.text import Text

console = Console()


def format_message_content(message):
    """Convert message content to displayable string."""
    parts = []
    tool_calls_processed = False

    # Handle main content
    if isinstance(message.content, str):
        parts.append(message.content)
    elif isinstance(message.content, list):
        # Handle complex content like tool calls (Anthropic format)
        for item in message.content:
            if item.get("type") == "text":
                parts.append(item["text"])
            elif item.get("type") == "tool_use":
                parts.append(f"\n🔧 Tool Call: {item['name']}")
                parts.append(f"   Args: {json.dumps(item['input'], indent=2)}")
                parts.append(f"   ID: {item.get('id', 'N/A')}")
                tool_calls_processed = True
    else:
        parts.append(str(message.content))

    # Handle tool calls attached to the message (OpenAI format) - only if not already processed
    if (
        not tool_calls_processed
        and hasattr(message, "tool_calls")
        and message.tool_calls
    ):
        for tool_call in message.tool_calls:
            parts.append(f"\n🔧 Tool Call: {tool_call['name']}")
            parts.append(f"   Args: {json.dumps(tool_call['args'], indent=2)}")
            parts.append(f"   ID: {tool_call['id']}")

    return "\n".join(parts)


def format_messages(messages):
    """Format and display a list of messages with Rich formatting."""
    for m in messages:
        msg_type = m.__class__.__name__.replace("Message", "")
        content = format_message_content(m)

        if msg_type == "Human":
            console.print(Panel(content, title="🧑 Human", border_style="blue"))
        elif msg_type == "Ai":
            console.print(Panel(content, title="🤖 Assistant", border_style="green"))
        elif msg_type == "Tool":
            console.print(Panel(content, title="🔧 Tool Output", border_style="yellow"))
        else:
            console.print(Panel(content, title=f"📝 {msg_type}", border_style="white"))


def format_message(messages):
    """Alias for format_messages for backward compatibility."""
    return format_messages(messages)


def show_prompt(prompt_text: str, title: str = "Prompt", border_style: str = "blue"):
    """Display a prompt with rich formatting and XML tag highlighting.

    Args:
        prompt_text: The prompt string to display
        title: Title for the panel (default: "Prompt")
        border_style: Border color style (default: "blue")
    """
    # Create a formatted display of the prompt
    formatted_text = Text(prompt_text)
    formatted_text.highlight_regex(r"<[^>]+>", style="bold blue")  # Highlight XML tags
    formatted_text.highlight_regex(
        r"##[^#\n]+", style="bold magenta"
    )  # Highlight headers
    formatted_text.highlight_regex(
        r"###[^#\n]+", style="bold cyan"
    )  # Highlight sub-headers

    # Display in a panel for better presentation
    console.print(
        Panel(
            formatted_text,
            title=f"[bold green]{title}[/bold green]",
            border_style=border_style,
            padding=(1, 2),
        )
    )


def extract_todos_from_state(state: dict) -> list:
    """Extract todos from agent state.

    Args:
        state: The agent state dictionary from agent.invoke() result

    Returns:
        List of todo items, each with 'content' and 'status' fields
    """
    # Todos are stored in the state under the 'todos' key by TodoListMiddleware
    todos = state.get("todos", [])
    return todos


def format_todos_as_markdown(todos: list, research_question: str = None) -> str:
    """Format todos as a markdown document.

    Args:
        todos: List of todo items from extract_todos_from_state()
        research_question: Optional research question to include at the top

    Returns:
        Formatted markdown string
    """
    lines = []
    
    if research_question:
        lines.append(f"# Research Plan")
        lines.append("")
        lines.append(f"## Research Question")
        lines.append("")
        lines.append(research_question)
        lines.append("")
    
    lines.append("## Todo List")
    lines.append("")
    
    if not todos:
        lines.append("*No todos found*")
    else:
        # Group by status
        status_groups = {
            "completed": [],
            "in_progress": [],
            "pending": [],
        }
        
        for todo in todos:
            status = todo.get("status", "pending")
            content = todo.get("content", "")
            if status in status_groups:
                status_groups[status].append(content)
            else:
                status_groups["pending"].append(content)
        
        # Display in order: pending, in_progress, completed
        for status, label in [
            ("pending", "📋 Pending"),
            ("in_progress", "🔄 In Progress"),
            ("completed", "✅ Completed"),
        ]:
            items = status_groups[status]
            if items:
                lines.append(f"### {label}")
                lines.append("")
                for item in items:
                    lines.append(f"- {item}")
                lines.append("")
    
    return "\n".join(lines)


def save_todos_to_file(state: dict, filepath: str = "/research_plan.md", research_question: str = None):
    """Extract todos from state and save to a file.

    Args:
        state: The agent state dictionary from agent.invoke() result
        filepath: Path to save the research plan (default: "/research_plan.md")
        research_question: Optional research question to include
    """
    todos = extract_todos_from_state(state)
    markdown = format_todos_as_markdown(todos, research_question)
    
    # Use write_file tool or direct file write
    # For programmatic use, you might want to use standard file I/O
    with open(filepath.lstrip("/"), "w") as f:
        f.write(markdown)
    
    return filepath


def count_subagent_calls(result: dict) -> dict:
    """Count how many sub-agent calls were made in the agent execution.

    Args:
        result: The agent result dictionary from agent.invoke()

    Returns:
        Dictionary with counts and details:
        - total_calls: Total number of task() calls
        - calls_by_round: List of counts per delegation round
        - max_parallel: Maximum number of parallel calls in a single round
    """
    messages = result.get("messages", [])
    task_calls = []
    
    for message in messages:
        # Check for tool calls in message content (Anthropic format)
        if isinstance(message.content, list):
            for item in message.content:
                if item.get("type") == "tool_use" and item.get("name") == "task":
                    task_calls.append(item)
        
        # Check for tool_calls attribute (OpenAI format)
        if hasattr(message, "tool_calls") and message.tool_calls:
            for tool_call in message.tool_calls:
                if tool_call.get("name") == "task":
                    task_calls.append(tool_call)
    
    # Group calls by message to identify parallel calls
    calls_by_message = {}
    for i, message in enumerate(messages):
        message_calls = []
        if isinstance(message.content, list):
            for item in message.content:
                if item.get("type") == "tool_use" and item.get("name") == "task":
                    message_calls.append(item)
        if hasattr(message, "tool_calls") and message.tool_calls:
            for tool_call in message.tool_calls:
                if tool_call.get("name") == "task":
                    message_calls.append(tool_call)
        if message_calls:
            calls_by_message[i] = len(message_calls)
    
    calls_by_round = list(calls_by_message.values()) if calls_by_message else []
    max_parallel = max(calls_by_round) if calls_by_round else 0
    
    return {
        "total_calls": len(task_calls),
        "total_rounds": len(calls_by_round),
        "calls_by_round": calls_by_round,
        "max_parallel": max_parallel,
        "details": [
            {
                "round": i + 1,
                "subagents": count,
                "parallel": count > 1
            }
            for i, count in enumerate(calls_by_round)
        ]
    }


def print_subagent_summary(result: dict):
    """Print a summary of sub-agent usage.

    Args:
        result: The agent result dictionary from agent.invoke()
    """
    stats = count_subagent_calls(result)
    
    console.print(Panel(
        f"""
📊 Sub-Agent Usage Summary

Total Sub-Agent Calls: {stats['total_calls']}
Delegation Rounds: {stats['total_rounds']}
Max Parallel Calls: {stats['max_parallel']}

Breakdown by Round:
{chr(10).join([f"  Round {d['round']}: {d['subagents']} sub-agent(s) {'(parallel)' if d['parallel'] else ''}" for d in stats['details']])}
        """.strip(),
        title="🤖 Sub-Agent Statistics",
        border_style="cyan"
    ))
