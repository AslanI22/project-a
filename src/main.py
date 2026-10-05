"""Главный модуль Task Manager."""

from models import Task
from utils import format_task

from project_b_utils import get_current_date, reverse_string, to_upper


def main():
    tasks = [
        Task(1, "Изучить Git Submodules", done=False),
        Task(2, "Написать отчёт по лабе", done=True),
    ]
    for task in tasks:
        print(format_task(task))

    print()
    print(f"Сегодня: {get_current_date()}")
    print(f"Реверс: {reverse_string('Task Manager')}")
    print(f"Верхний регистр: {to_upper('project b v1.0.1')}")


if __name__ == "__main__":
    main()