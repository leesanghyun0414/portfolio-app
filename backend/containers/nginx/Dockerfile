ARG NGINX_VERSION=1.21.1-alpine

FROM nginx:${NGINX_VERSION} as nginx

# CONFIGURE FILES
COPY ./backend/containers/nginx/conf /etc/nginx/conf.d
COPY ./backend/containers/nginx/uwsgi_params /etc/nginx/uwsgi_params

# APP SCRIPT DIRECTORIES
RUN mkdir /var/www \
    && mkdir /var/www/static /var/www/front
