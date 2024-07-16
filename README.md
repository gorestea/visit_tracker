# Visit Tracker API

## Описание
API для мобильного приложения, в котором полевой сотрудник будет выполнять визиты в магазины.

## Технологии
- Python 3.9
- Django 3.x
- Django REST Framework
- PostgreSQL

## Установка и запуск

### Локально

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-repo/visit-tracker.git
    cd visit-tracker
    ```

2. Создайте виртуальное окружение и активируйте его:
    ```bash
    python3 -m venv venv
    source venv/bin/activate  # Для Windows используйте `venv\Scripts\activate`
    ```

3. Установите зависимости:
    ```bash
    pip install -r requirements.txt
    ```

4. Настройте `.env`:
    ```ini
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:password@localhost:5432/mydatabase
    ```

5. Примените миграции (включая создание тестовых данных):
    ```bash
    python manage.py migrate
    ```

6. Создайте суперпользователя:
    ```bash
    python manage.py createsuperuser
    ```

7. Запустите сервер разработки:
    ```bash
    python manage.py runserver
    ```

### Использование Docker

1. Клонируйте репозиторий:
    ```bash
    git clone https://github.com/your-repo/visit-tracker.git
    cd visit-tracker
    ```

2. Создайте файл `.env` на основе `.env.example` и настройте его:
    ```ini
    DEBUG=True
    SECRET_KEY=your_secret_key
    DATABASE_URL=postgres://user:password@db:5432/mydatabase
    ```

3. Запустите контейнеры Docker:
    ```bash
    docker-compose up --build
    ```

4. Примените миграции и создайте суперпользователя (выполните в новом терминале):
    ```bash
    docker-compose exec web python manage.py migrate
    docker-compose exec web python manage.py createsuperuser
    ```

## Документация API

Для просмотра документации API перейдите по адресу `http://localhost:8000/swagger/` после запуска сервера.

## Тестовые данные

При применении миграций автоматически создаются тестовые данные:
- Работник: Тестовый Работник (номер телефона: 123456789)
- Торговые точки: Тестовая Торговая Точка 1, Тестовая Торговая Точка 2
- Посещения для каждой торговой точки
