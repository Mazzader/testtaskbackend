Запуск

docker-compose up -f docker-compose.yml [-f docker-compose.prod.yml]

Деплой

    Скопировать проект в /opt/rest;
    Проверить, что все работает;
    Скопировать config/rest.service в /etc/systemd/system/;
    Выполнить systemctl enable --now rest.

Gunicorn

Gunicorn как WSGI Server.
Пояснение

Два конфига для docker-compose. Один используется для разработки, второй подключается к первому на проде. Это нужно, чтобы:

    не запускать Nginx на 80 порту на своем компе;
    разделить переменные окружения базы (для прода и разработки), чтобы не тащить секретные данные в гит.
