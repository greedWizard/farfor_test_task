# Тестовое задание https://github.com/smenateam/assignments/blob/master/backend/README.md

## Stack

* python = "3.10.4"
* Django = "^4.0.6"
* python-dotenv = "^0.20.0"
* psycopg2 = "^2.9.3"
* djangorestframework = "^3.13.1"
* django-rq = "^2.5.1"
* requests = "^2.28.1"
* django-filter = "^22.1"


## Запуск проекта

Проект работает на poetry, любые команды нужно запускать не напрямую,а через ```poetry run```

* Добавить .env файл (пример лежит в корне)
* Добавить файл ```core/project/settings/local.py``` (пример лежит в той же папке)
* ```docker-compose build && docker-compose up``` - запускаем сторонние сервисы (бд, редис)
* ```poetry run pyhon manage.py runserver 0.0.0.0:8000``` - запускаем сам проект
* ```poetry run python manage.py rqworker default``` - запускаем воркер для обработки задачи django_rq

Схема полностью соответствует https://editor.swagger.io/

## Тесты

```poetry run python manage.py test --keepdb``` (Реализованы не все тесты, только создание чека)
