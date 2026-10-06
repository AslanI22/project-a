"""Flask-приложение Task Manager с использованием project-b-utils."""

from datetime import datetime
from flask import Flask, render_template, request, redirect, url_for

from models import Task
from project_b_utils import (
    get_current_date,
    format_date,
    days_between,
    reverse_string,
    count_words,
    to_upper,
    get_logger,
    log_event,
)

app = Flask(__name__, template_folder="../templates")
logger = get_logger("project_a", log_dir="logs")

# In-memory хранилище задач (для лабы)
TASKS = [
    Task(1, "Изучить Git Submodules", done=False, priority=2, due_date="2026-10-10"),
    Task(2, "Настроить CI/CD", done=True, priority=1, due_date="2026-10-07"),
    Task(3, "Написать отчёт по лабе", done=False, priority=3, due_date="2026-10-15"),
]
_next_id = 4


def _task_stats(tasks):
    """Возвращает статистику по задачам."""
    total = len(tasks)
    done = sum(1 for t in tasks if t.done)
    overdue = 0
    today = datetime.now()
    for t in tasks:
        if t.due_date and not t.done:
            try:
                due = datetime.strptime(t.due_date, "%Y-%m-%d")
                if days_between(today, due) > 0 and due < today:
                    overdue += 1
            except ValueError:
                pass
    return {"total": total, "done": done, "overdue": overdue}


@app.route("/")
def index():
    stats = _task_stats(TASKS)
    log_event(logger, f"Открыт главный экран, задач: {stats['total']}")
    return render_template(
        "index.html",
        tasks=TASKS,
        stats=stats,
        today=get_current_date(),
        today_formatted=format_date(datetime.now()),
    )


@app.route("/add", methods=["POST"])
def add_task():
    global _next_id
    title = request.form.get("title", "").strip()
    if not title:
        return redirect(url_for("index"))

    due_date = request.form.get("due_date", "")
    try:
        priority = int(request.form.get("priority", 3))
    except ValueError:
        priority = 3

    TASKS.append(
        Task(_next_id, title, done=False, priority=priority, due_date=due_date)
    )
    log_event(logger, f"Добавлена задача #{_next_id}: {title}")
    _next_id += 1
    return redirect(url_for("index"))


@app.route("/toggle/<int:task_id>")
def toggle_task(task_id):
    for t in TASKS:
        if t.id == task_id:
            t.done = not t.done
            log_event(logger, f"Задача #{task_id} -> done={t.done}")
            break
    return redirect(url_for("index"))


@app.route("/tools", methods=["GET", "POST"])
def tools():
    """Демонстрация функций project-b."""
    result = {}
    if request.method == "POST":
        text = request.form.get("text", "")
        result = {
            "original": text,
            "reversed": reverse_string(text),
            "upper": to_upper(text),
            "words": count_words(text),
        }
        log_event(logger, f"Tools: обработка текста длиной {len(text)}")
    return render_template("tools.html", result=result)


if __name__ == "__main__":
    log_event(logger, "Запуск Flask-приложения")
    app.run(debug=True, port=5000)