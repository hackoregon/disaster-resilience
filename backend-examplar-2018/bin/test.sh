#! /bin/bash
usage() { echo "Usage: $0 [-d] for a development test, [-p] for production test" 1>&2; exit 1; }

while getopts ":dp" opt; do
    case "$opt" in
        d)
          docker-compose -p tests run --entrypoint /code/bin/test-entrypoint.sh  -p 8000 --rm api
          echo "Stopping test db container"
          docker stop tests_db_1
          echo "Removing test db container"
          docker rm tests_db_1
           ;;
        p)
          docker-compose -p tests run --entrypoint /code/bin/test-entrypoint.sh  -p 8000 --all -f
          echo "Stopping test db container"
          docker stop tests_db_1
          echo "Removing test db container"
          docker rm tests_db_1
          ;;
        *)
          usage
          ;;
    esac
done
