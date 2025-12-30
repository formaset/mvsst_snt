# Сайт АНО «МосводостокСтройТрест»

Проект на Django + Wagtail для сайта организации АНО по развитию городской среды «МосводостокСтройТрест».

## Быстрый старт

```bash
python -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cp .env.example .env
python manage.py migrate
python manage.py createsuperuser
python manage.py bootstrap_site
python manage.py runserver
```

Откройте `http://localhost:8000/`.

## Сборка статики

```bash
python manage.py collectstatic
```

Статика будет собрана в `staticfiles/`.

## Настройка пути админки

Переменная окружения `ADMIN_PATH` задаёт путь админки Wagtail (по умолчанию `control/`).

```bash
export ADMIN_PATH=control/
```

## Переключение на MySQL

В `.env` укажите параметры базы:

```env
DB_ENGINE=django.db.backends.mysql
DB_NAME=mvsst
DB_USER=root
DB_PASSWORD=secret
DB_HOST=127.0.0.1
DB_PORT=3306
```

## Загрузка медиа

Загруженные изображения и видео попадают в `MEDIA_ROOT` (`media/`).
Для переноса медиа на сервер достаточно скопировать папку `media/`.

## Bootstrap контент

Команда `bootstrap_site` создаёт структуру страниц, пример новости, руководителя и награды, а также группу «Редактор новостей».

```bash
python manage.py bootstrap_site
```
