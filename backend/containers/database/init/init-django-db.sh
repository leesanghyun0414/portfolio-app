#!/usr/bin/env bash

# Exit immediately if a command exits with a non-zero status.
#set -e
#
#psql -v ON_ERROR_STOP=1 --username "$POSTGRES_USER" --dbname "$POSTGRES_DB" << EOSQL
#    alter database $POSTGRES_DB set timezone to "Asia/Tokyo";
#EOSQL

echo "test"