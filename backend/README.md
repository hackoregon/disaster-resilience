# Disaster Resilience 2018 Backend Applicaton Server

Simple backend Django+DRF application to serve disaster-resilience data through a REST API.

## Usage

### Development

1. Clone repo
2. Place copy of disaster-resilience database backup in Backups/ directory.
3. Execute `bin/start.sh -d` to build and start both the database and application images. Once this has finished successfully, you can browse to the API on your local machine.

## History

This repo represents the work of many members of the Hack Oregon project team. The roots of this work began with the [2017 backend-service-pattern](https://github.com/hackoregon/backend-service-pattern), the work of the DevOps and platform teams, and the APIs deployed for the 2017 seasons.

The current implementation's application and database docker images were generated from the [backend-exemplar-2018](https://github.com/hackoregon/backend-exemplar-2018) repo, which is based on the [transportation-system-backend](https://github.com/hackoregon/transportation-system-backend) and [passenger_census_api](https://github.com/hackoregon/passenger_census_api) repos. The database structure is an implementation of the PostGIS container of the [data-science-pet-containers](https://github.com/hackoregon/data-science-pet-containers) repo.


## Major Contributors

Nathan Miller ([nam20485](https://github.com/nam20485))
M. Edward (Ed) Borasky ([znmeb](https://github.com/znmeb))