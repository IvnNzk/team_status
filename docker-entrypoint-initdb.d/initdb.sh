#!/bin/bash
set -e

psql -v ON_ERROR_STOP=1 --username $POSTGRES_USER <<-EOSQL
    CREATE DATABASE team_status_web_app_db;
    GRANT ALL PRIVILEGES ON DATABASE team_status_web_app_db to $POSTGRES_USER;
EOSQL
