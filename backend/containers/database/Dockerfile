ARG POSTGRES_VERSION=14.0-alpine

FROM postgres:${POSTGRES_VERSION} as postgres

COPY ./backend/containers/database/init/init-django-db.sh /docker-entrypoint-initdb.d/init-django-db.sh


