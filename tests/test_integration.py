"""Интеграционные тесты Flask-приложения с project-b."""

import sys
import os

sys.path.insert(0, os.path.join(os.path.dirname(__file__), "..", "src"))

from app import app


def test_index_page():
    client = app.test_client()
    resp = client.get("/")
    assert resp.status_code == 200
    assert "Task Manager".encode("utf-8") in resp.data


def test_tools_page_get():
    client = app.test_client()
    resp = client.get("/tools")
    assert resp.status_code == 200


def test_tools_page_processes_text():
    client = app.test_client()
    resp = client.post("/tools", data={"text": "hello world"})
    assert resp.status_code == 200
    assert b"dlrow olleh" in resp.data  # reverse_string
    assert b"HELLO WORLD" in resp.data  # to_upper
    assert b"2" in resp.data            # count_words


def test_add_task():
    client = app.test_client()
    resp = client.post("/add", data={"title": "Test task", "priority": "1"}, follow_redirects=True)
    assert resp.status_code == 200
    assert b"Test task" in resp.data