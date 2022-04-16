
ARG NODE_VERSION=17-alpine3.14

FROM node:${NODE_VERSION} as build-stage

RUN apk update \
&& apk upgrade

ARG PRODUCTION

WORKDIR /usr/app

# PACKAGE FILE
COPY frontend/package*.json .

# PACKAGE INSTALLER
COPY scripts/common/frontend/build.sh /usr/app/build.sh
RUN chmod 777 build.sh

COPY frontend .

RUN ["/usr/app/build.sh"]



FROM node:${NODE_VERSION} as dev-stage

WORKDIR /usr/app

# ENTRYPOINT SCRIPT
COPY scripts/dev/frontend/entrypoint.sh .

# MODULES
COPY --from=build-stage /usr/app/node_modules ./node_modules

# APP
COPY frontend .


ENTRYPOINT ["/usr/app/entrypoint.sh"]


FROM node:${NODE_VERSION} as prod-stage

WORKDIR /usr/app

# BUILDED APP
COPY --from=build-stage /usr/app/src/dist /usr/app/dist



FROM node:${NODE_VERSION} as interpreter_stage

WORKDIR /usr/app

COPY frontend/package.json /usr/app

# MODULES
COPY --from=build-stage /usr/app/node_modules ./node_modules

