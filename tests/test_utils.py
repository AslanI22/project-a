"""Тесты для Project B."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from datetime import datetime

from date_utils import format_date
from string_utils import reverse_string, capitalize_words


def test_reverse_string():
    assert reverse_string("Hello") == "olleH"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_format_date():
    dt = datetime(2026, 10, 5)
    assert format_date(dt) == "05.10.2026"
    assert format_date(dt, "%Y-%m-%d") == "2026-10-05"