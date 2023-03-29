FROM nginx:latest

# общий файл настроек
# COPY nginx.conf /etc/nginx/nginx.conf 

# !!! в официальном образе sites-available и sites-enabled не подключены

COPY foxeye.prod.conf /etc/nginx/conf.d/default.conf

ENV TZ=Europe/Moscow