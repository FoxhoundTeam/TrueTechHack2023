[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

# Проект FoxEye

## Описание

Решение команды Foxhound на хакатоне MTC True Tech Hack (https://true-tech-hack.ru/), 24-31 марта 2023 г. Демонстрационное приложение доступно на http://foxhound-team.pro до конца хакатона. Веб-приложение обеспечивает демонстрацию возможностей алгоритмов, реализованных командой, по адаптации видео для людей с особыми запросами по состоянию здоровья при онлайн-просмотре.

<img width="1024" alt="image" src="https://user-images.githubusercontent.com/26321368/228475641-6b21bf28-2a3d-4024-81ac-e0fe2b0a3c8a.png">

## Развёртывание

1. Установить [docker  и docker compose](https://docs.docker.com/engine/install/ubuntu/).
2. В папке compose создать файл .env и [заполнить](#описание-переменных-окружения) его в соответствии с примерами.
3. Запустить команду docker compose up -d с правами суперпользователя:
```bash
sudo docker compose -f docker-compose.prod.yml up -d
```

## Структура каталогов

* `backend` - файлы бекенда на DjangoREST и Docker-файл для его развёртывания
* `frontend` - файлы фронтенда на Vuejs + Vuetify и Docker-файл для его развёртывания
* `nginx` - файлы конфигурации nginx и Docker-файл для его развёртывания
* `postgres` - файлы инициализации БД и Docker-файл для её развёртывания
* `research` - файлы jupyter и python для отладки и демонстрации алгоритмов фильтрации
    * `Content_Sergey` - файлы для обучения и инференса фильтра контента (курение), и обученные веса
    * `Flickering_Mihail` - файлы для отработки и демонстрации алгоритма 1 темпорального сглаживания мерцания, опасного при эпилепсии
    * `Flickering_Yaroslav` - файлы для отработки и демонстрации алгоритма 2 темпорального сглаживания мерцания, опасного при эпилепсии
* `serv_settings` - файлы для настройки сервера gunicorn
* `docker-compose.prod.yml` - файл docker compose для автоматизации развёртывания веб-приложени

## Команда

* Антон Недогарок - фуллстек (DjangoREST, Vuejs, Vuetify)
* Зеленовский Сергей - ML-инженер
* Халманский Ярослав - алгоритмическое обеспечение, Python
* Анисимов Михаил - алгоритмическое обеспечение, Python
