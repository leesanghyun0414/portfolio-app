ARG NGINX_VERSION=1.21.1-alpine

ARG NODE_VERSION=17-alpine3.14


FROM nginx:${NGINX_VERSION} as nginx

# CONFIGURE FILES
COPY ./backend/containers/nginx/conf/dev /etc/nginx/conf.d
COPY ./backend/containers/nginx/uwsgi_params /etc/nginx/uwsgi_params

# APP SCRIPT DIRECTORIES
RUN mkdir /var/www \
    && mkdir /var/www/static /var/www/front






FROM node:${NODE_VERSION} as build-stage

ARG VITE_ASSET_ROOT
ARG VITE_API_SERVER

ENV VITE_ASSET_ROOT=${VITE_ASSET_ROOT}
ENV VITE_API_SERVER=${VITE_API_SERVER}

RUN apk update \
&& apk upgrade

ARG PRODUCTION=1

WORKDIR /usr/app

# PACKAGE FILE
COPY frontend/package*.json .

# PACKAGE INSTALLER
COPY scripts/common/frontend/build.sh /usr/app/build.sh
RUN chmod 777 build.sh

COPY frontend .

RUN ["/usr/app/build.sh"]

FROM nginx:${NGINX_VERSION} as nginx_prod

# CONFIGURE FILES
COPY ./backend/containers/nginx/conf/prod/default.conf /etc/nginx/conf.d/default.conf
COPY ./backend/containers/nginx/conf/prod/nginx.conf /etc/nginx/nginx.conf

COPY ./backend/containers/nginx/uwsgi_params /etc/nginx/uwsgi_params

RUN chown -R 101:0 /var/cache/nginx \
    && chmod -R g+w /var/cache/nginx

# APP SCRIPT DIRECTORIES
RUN mkdir /var/www \
    && mkdir /var/www/static /var/www/front

#COPY ./frontend/src/dist /var/www/front
COPY --from=build-stage /usr/app/src/dist /var/www/front



# Heroku not support bind port, define $PORT to synchronous port.
# For container stopping solution, add config daemon off.
CMD sed -i -e 's/$PORT/'"$PORT"'/g' /etc/nginx/conf.d/default.conf && nginx -g 'daemon off;'


USER 101

