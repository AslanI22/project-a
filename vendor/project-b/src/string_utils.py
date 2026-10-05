"""Утилиты для работы со строками."""


def reverse_string(s: str) -> str:
    """Возвращает строку в обратном порядке."""
    return s[::-1]


def capitalize_words(s: str) -> str:
    """Делает первую букву каждого слова заглавной."""
    return s.title()

def count_words(s: str) -> int:
    """Возвращает количество слов в строке."""
    return len(s.split())