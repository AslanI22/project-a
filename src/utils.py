"""Утилиты."""

from models import Task


def format_task(task: Task) -> str:
    status = "[x]" if task.done else "[ ]"
    return f"{status} #{task.id}: {task.title}"