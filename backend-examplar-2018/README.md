# Example Geo-Capable Django REST framework (DRF) API using Docker

This is a simple example repo to quickstart a [DRF](http://www.django-rest-framework.org/) API within a Docker container.

Allows for multiple environments to run API, through series of docker-compose files. You should be able to replace the Django Code, making a few updates and get this running with a new API or existing one.

## Main Parts of Repo

DOCKER related:

* `env.sample` - A sample env file to setup environmental variables
* bin directory - directory containing the startup and entrypoint scripts:
  * `build.sh` - This script runs a `docker-compose build` command, accepts 2 flags:
    * `-d` - Builds containers based on the `development-docker-compose.yml` file
    * `-p` - Builds containers based on the `production-docker-compose.yml` file
  * `start.sh` - This script runs a `docker-compose up` command, starting the containers and apps, accepts 2 flags:
    * `-d` - Starts containers based on the `development-docker-compose.yml` file
    * `-p` - Starts containers based on the `production-docker-compose.yml` file
  * `test.sh` - This script spins up and runs tests in test containers. and removes test container once the script is complete
  * Entrypoint scripts - These are run within the api container when `docker-compose up` is run:
    * `development-docker-entrypoint.sh` - Startup tasks for development container
    * `production-docker-entrypoint.sh` - Startup tasks for production container
    * `test-entrypoint.sh` -  Startup tasks for testing container
  * `create-api-project.sh` - Script which will remove the sample app and create a new api with specified project name. It assumes the default app created will be named `api`.
  * `remove-sample.sh` - This script removes the sample application - is called as part of the `create-api-project.sh` script.
* Backups directory - directory where you can store any database backups to restore into the local database Container; also contains the database restore script
* Docker-Compose Files -  2 files which compose containers and networking for each environment:
  * `development-docker-compose.yml` - This is a local dev environment, will spin up a local api container connecting with a local db. It will run the Django Dev Server with the DEBUG variable set to True.
  * `production-docker-compose.yml` - This is set to run a production-like environment, creating a api container running with gunicorn server, and green database pooling. It removes the local development database from the stack, connecting to a remote database for which the variables/creds are entered into the production vars in the `.env` file
* DOCKERFILEs:
  * `DOCKERFILE.db.development` - The DOCKERFILE for local database container
  * `DOCKERFILE.api.development` - The DOCKERFILE for local api container
  * `DOCKERFILE.api.production` - The DOCKERFILE for a production build of api

API Related:

* `gunicorn_config.py` - Config file for the gunicorn server

## Run the Sample

There is currently a Sample API included within the repo. To run:

1. First `cd` into the root directory of your clone of the repo and run the command `cp env.sample .env`

2. Build the development containers using the command: `./bin/build.sh -d`. If this script won't run, you may need to confirm you have executable perms on all the scripts in the `./bin` folder: `$ chmod +x ./bin/*.sh` Feel free to read each one and assign perms individually, 'cause it is your computer :stuck_out_tongue_winking_eye: and security is a real thing.

3. Once this completes you will now want to start up the project. We will use the `start.sh` script for this, again using the `-d` flag to run locally:  `./bin/start.sh -d` The first time you run this you will see the database restores. You will also see the api container start up.

4. Open your browser and you will be able to access the Django REST framework browserable front end. The IP address you use will depend on your Docker hosting:

    * Windows 10 Pro + Docker for Windows, MacOS or Linux: API root `http://localhost:8000/api`, Swagger API schema `http://localhost:8000/schema`
    * Docker Toolbox running on Windows or Mac: API root `http://MACHINE-IP:8000/api`, Swagger API schema `http://MACHINE-IP:8000/schema`

        where `MACHINE-IP` is the IP address `docker-machine ip` returns.

5. You can stop the container using Ctrl-C to stop the process in the terminal window.

## Quickstart for your own API - Development

Once you understand the sample you can create your own api. Once you do this it will delete the sample, replacing the files with your own. NOTE: at this point you should no longer commit changes to the original repo.

1. `cp env.sample .env` in the root of the repo (this file is already in the `.gitignore`, so you should not have to worry about it getting accidentally checked into a GitHub repo)

2. Edit your `.env` file and change the `DEVELOPMENT_` variables to appropriate values for your project - feel free to ignore the `PRODUCTION_` variables for the moment:

```shell
# MUST BE A DOCKER PROJECT NAME COMPLIANT NAME
PROJECT_NAME=<What you want to name the project>

# keep as true to run the Django dev server
DEBUG=True

# the database superuser name - this is the default
DEVELOPMENT_POSTGRES_USER=postgres

# the database name the API will connect to - "dbname" in most PostgreSQL command-line tools
DEVELOPMENT_POSTGRES_NAME=<your_database_name>

# *service* name (*not* image name) of the database in the Docker network
DEVELOPMENT_POSTGRES_HOST=db_development

# port the database is listening on in the Docker network
DEVELOPMENT_POSTGRES_PORT=5432

# password for the PostgreSQL database superuser in the database container
DEVELOPMENT_POSTGRES_PASSWORD=sit-down-c0mic

# Django secret key in the API container
DEVELOPMENT_DJANGO_SECRET_KEY=r0ck.ar0und.the.c10ck
```

3. Copy your database backup file into the backup folder. Database container is a PostGIS-enabled 9.6 container. Backup can be a .backup, .sql, or .sql.gz format.

4. Run the create-project script: `./bin/create-api-project.sh` (This will delete all files related to the sample app and replace with a new Django REST framework app with your project name. It will also replace the default `settings.py` file with the `sample.py`, which has been pre-configured a bit for our stack.)

5. This would be a good point to instantiate a new Git history for the project going forward. You can remove the existing git by removing the hidden folder - make sure you are in the repo directory and run `rm -rf .git`. You can then run `git init` to start a new history and then add your remote branch.

6. Create your api code. Checkout the [Django REST framework Guide](http://www.django-rest-framework.org/) on how to proceed.

7. Once this completes you will now want to start up the project. We will use the `start.sh` script for this, again using the `-d` flag to run locally:  `./bin/start.sh -d` The first time you run this you will see the database restores. You will also see the api container start up.

## Contributors and History

This repo represents the work of many members of the Hack Oregon project team. The roots of this work began with the [2017 backend-service-pattern](https://github.com/hackoregon/backend-service-pattern), the work of the DevOps and platform teams, and the APIs deployed for the 2017 seasons.

This current implementation builds on the [transportation-system-backend](https://github.com/hackoregon/transportation-system-backend) and [passenger_census_api](https://github.com/hackoregon/passenger_census_api). The database structure is an implementation of the PostGIS container of the **data-science-pet-containers** repo.

### Major Contributors

M. Edward (Ed) Borasky ([znmeb](https://github.com/znmeb)),
Brian Grant ([bhgrant8](https://github.com/bhgrant8), [BrianHGrant](https://github.com/BrianHGrant)),
Adi ([kiniadit](https://github.com/kiniadit)),
Mike Lonergan ([mikethecanuck](https://github.com/mikethecanuck)),
Alec Peters ([adpeters](https://github.com/adpeters))
