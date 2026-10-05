"""Главный модуль Task Manager."""

from models import Task
from utils import format_task


def main():
    tasks = [
        Task(1, "Изучить Git Submodules", done=False),
        Task(2, "Написать отчёт по лабе", done=True),
    ]
    for task in tasks:
        print(format_task(task))


if __name__ == "__main__":
    main()