#! /bin/bash

# create the users we'll be restoring to!
for user in $DB_USERS_TO_CREATE
do
  echo "Creating database user $user"
  createuser --no-createdb --no-createrole --no-superuser --no-replication $user
  command="ALTER USER \"$user\" WITH PASSWORD '${TEAM_PASSWORD}';"
  psql -c "$command"
done
