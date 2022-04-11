ARG PYTHON_VERSION=3.9.7-buster
FROM python:${PYTHON_VERSION} as build_stage

ENV WORKDIR=/usr/app

WORKDIR $WORKDIR

# PYTHON ENVS
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# DEBIAN PACKAGES UPDATE
RUN apt update

# PACKAGES INSTALL
RUN pip install --upgrade pip \
&& pip install pipenv

COPY ./backend/containers/django/Pipfile /usr/app/Pipfile

RUN pipenv install --skip-lock --system --dev --pre

RUN pip uninstall -y pipenv



FROM python:3.9.7-slim-buster as dev_stage

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/app

# BUILDED FILES
COPY --from=build_stage /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build_stage /usr/local/bin /usr/local/bin
COPY --from=build_stage /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu
COPY --from=build_stage /lib/x86_64-linux-gnu/libkeyutils.so.1 /lib/x86_64-linux-gnu/libkeyutils.so.1
COPY --from=build_stage /lib/x86_64-linux-gnu/libkeyutils.so.1.8 /lib/x86_64-linux-gnu/libkeyutils.so.1.8

# HOST MACHINE FILES
COPY ./backend/containers/django /usr/app
COPY ./scripts/dev/backend/entrypoint.sh /usr/app/entrypoint.sh
COPY ./scripts/common/django/common.sh /usr/app/common.sh
COPY ./scripts/dev/backend/superuser-init.sh /usr/app/superuser-init.sh

RUN chmod 774 /usr/app/entrypoint.sh


# CREATE USER AND GROUP FOR COMMUNICATION TO NGINX
RUN groupadd -g 1000 nginx && \
    useradd -m -s /bin/bash -u 1000 -g 1000 -G sudo nginx && \
    echo "nginx:nginx" | chpasswd


RUN chown nginx /tmp

ENTRYPOINT ["/usr/app/entrypoint.sh"]


FROM python:3.9.7-slim-buster as prod_stage

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /usr/app

# BUILDED FILES
COPY --from=build_stage /usr/local/lib/python3.9/site-packages /usr/local/lib/python3.9/site-packages
COPY --from=build_stage /usr/local/bin /usr/local/bin
COPY --from=build_stage /usr/lib/x86_64-linux-gnu /usr/lib/x86_64-linux-gnu
COPY --from=build_stage /lib/x86_64-linux-gnu/libkeyutils.so.1 /lib/x86_64-linux-gnu/libkeyutils.so.1
COPY --from=build_stage /lib/x86_64-linux-gnu/libkeyutils.so.1.8 /lib/x86_64-linux-gnu/libkeyutils.so.1.8

# HOST MACHINE FILES
COPY ./backend/containers/django /usr/app
COPY ./scripts/prod/backend/entrypoint.sh /usr/app/entrypoint.sh
COPY ./scripts/common/django/common.sh /usr/app/common.sh
COPY ./scripts/prod/backend/superuser-init.sh /usr/app/superuser-init.sh


RUN chmod 774 /usr/app/entrypoint.sh



# Create uwsgi runner user
RUN groupadd -g 1000 uwsgi && \
    useradd -m -s /bin/bash -u 1000 -g 1000 -G sudo uwsgi && \
    echo "uwsgi:uwsgi" | chpasswd

# CREATE IMAGE USER
RUN groupadd -g 1010 portp && \
    useradd -m -s /bin/bash -u 1010 -g 1010 -G sudo portp && \
    echo "portp:portp" | chpasswd



USER 1010

CMD uwsgi --http-socket 0.0.0.0:$PORT --module config.wsgi --py-autoreload 1 --processes 4 --uid=uwsgi --gid=uwsgi --max-requests=5000 --buffer-size=32768



