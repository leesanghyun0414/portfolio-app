#!/usr/bin/env sh

set -e

. ./common.sh

# Migration Process
migrations &
migration_task=$!
wait $migration_task
echo "Migration completed successfully!"