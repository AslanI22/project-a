# Project A — Task Manager

Веб-приложение для управления задачами на Flask. Использует библиотеку `project-b-utils`.

## Установка

1. Установите `project-b` (editable):
pip install -e ../project-b
2. Установите зависимости:
pip install -r requirements.txt

## Запуск
cd src
python app.py


Откройте http://127.0.0.1:5000

## Возможности

- Список задач с приоритетом и дедлайном
- Статистика (всего, выполнено, просрочено)
- Добавление и переключение задач
- Демонстрация функций project-b (реверс, upper, счёт слов)

## Тесты
pytest tests/ -v