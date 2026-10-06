# Project A — Task Manager

Веб-приложение для управления задачами на Flask.
Использует библиотеку [project-b](https://github.com/AslanI22/project-b) как pip-пакет.

## Возможности

- Список задач с приоритетом и дедлайном
- Статистика: всего / выполнено / просрочено
- Добавление и переключение статуса задач
- Страница «Инструменты» — демонстрация функций `project-b`
  (реверс строки, upper, счёт слов)
- Логирование операций в `logs/project_a.log`

## Установка

1. Клонируйте оба репозитория **рядом** друг с другом:
   ```bash
   git clone https://github.com/AslanI22/project-a.git
   git clone https://github.com/AslanI22/project-b.git
   ```

2. Создайте виртуальное окружение в `project-a` и активируйте:
   ```powershell
   cd project-a
   python -m venv venv
   .\venv\Scripts\Activate.ps1
   ```

3. Установите зависимости:
   ```powershell
   pip install -r requirements.txt
   ```

   `requirements.txt` содержит `-e ../project-b`, что устанавливает
   библиотеку в editable-режиме.

## Запуск

```powershell
cd src
python app.py
```

Откройте http://127.0.0.1:5000

## Тесты

```powershell
pytest tests/ -v
```

7 тестов: базовые (модели, утилиты) + интеграционные (Flask + project-b).

## Способы подключения project-b

В рамках лабораторной работы апробированы **три** способа:

| Способ | Папка | Обновление |
|---|---|---|
| **Git Submodule** | `libs/project-b/` | `cd libs/project-b && git pull` + коммит в A |
| **Git Subtree** (ветка `feature/subtree-approach`) | `vendor/project-b/` | `git subtree pull --prefix=vendor/project-b ...` |
| **Pip-пакет (editable)** | — | Автоматически при `pip install -e` |

В основном коде используется **pip-пакет** — это стандартный для Python подход.

## Структура

```
project-a/
├── libs/project-b/         ← git submodule
├── src/
│   ├── app.py              ← Flask
│   ├── main.py             ← консольная точка входа
│   ├── models.py
│   ├── utils.py
│   └── module_loader.py    ← демонстрация submodule-импорта
├── templates/
│   ├── base.html
│   ├── index.html
│   └── tools.html
├── tests/
│   ├── test_main.py
│   └── test_integration.py
├── requirements.txt
├── README.md
└── .gitignore
```