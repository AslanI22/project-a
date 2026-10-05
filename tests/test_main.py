"""Тесты для Task Manager."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from models import Task
from utils import format_task


def test_format_task_not_done():
    task = Task(1, "Test", done=False)
    assert format_task(task) == "[ ] #1: Test"


def test_format_task_done():
    task = Task(2, "Done", done=True)
    assert format_task(task) == "[x] #2: Done"


def test_task_default_not_done():
    task = Task(3, "Default")
    assert task.done is False