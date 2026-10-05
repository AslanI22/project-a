"""Загрузчик модулей из подмодуля project-b."""

import os
import sys

# Добавляем путь к исходникам подмодуля
_submodule_path = os.path.join(
    os.path.dirname(__file__),
    "..", "libs", "project-b", "src"
)
sys.path.insert(0, os.path.abspath(_submodule_path))

from date_utils import get_current_date, format_date
from string_utils import reverse_string, capitalize_words


def main():
    print(f"Текущая дата: {get_current_date()}")
    print(f"Обратный текст: {reverse_string('Hello World')}")
    print(f"С заглавной: {capitalize_words('hello world from project a')}")


if __name__ == "__main__":
    main()