"""Главный модуль Task Manager."""

from models import Task
from utils import format_task

# Импорт из установленного пакета project-b-utils
from project_b_utils import get_current_date, reverse_string


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


if __name__ == "__main__":
    main()