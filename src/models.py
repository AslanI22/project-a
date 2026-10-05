"""Модели данных."""

from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    due_date: str = ""  # Dev B: добавил дедлайн