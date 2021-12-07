#!/usr/bin/env sh

set -e

. ./common.sh
. ./superuser-init.sh

# Migration Process
migrations &
migration_task=$!
wait $migration_task
echo "Migration completed successfully!"

# If Not exists Django Superuser on Dev Container, Create
init_superuser &
init_superuser_task=$!
wait $init_superuser_task
echo "Django Superuser created successfully!"

cat <<EOF

uwsgi
-------------------------------
allow_host : $ALLOWED_HOSTS
PORT : 8081
DJANGO_DEBUG_MODE : $DEBUG

EOF

uwsgi --socket :8081 --module config.wsgi --py-autoreload 1 --processes 4 --uid=nginx --gid=nginx --max-requests=5000 \
--buffer-size=32768
