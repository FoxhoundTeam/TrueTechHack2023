FROM nginx:alpine
# RUN apt-get install certbot python3-certbot-nginx
RUN apk add certbot certbot-nginx

# общий файл настроек

# !!! в официальном образе sites-available и sites-enabled не подключены

# RUN apt install certbot python3-certbot-nginx
# RUN certbot --nginx -d foxhound-team.pro -d www.foxhound-team.pro

# MKDIR /etc/nginx/conf.d/www.foxhound-team.pro
# COPY foxeye.prod.conf /etc/nginx/conf.d/www.foxhound-team.pro/foxeye.prod.conf
# COPY nginx.conf /etc/nginx/conf.d/default.conf 

ENV TZ=Europe/Moscow