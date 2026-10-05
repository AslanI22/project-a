"""Модели данных."""

from dataclasses import dataclass


@dataclass
class Task:
    id: int
    title: str
    done: bool = False
    priority: int = 3  # Dev A: добавил приоритет