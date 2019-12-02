# Sample multi migrations projects

The example project consists of 2 python flask services that are using DB migrations powered by alembic.

## Setup

The project uses pipenv for the local dev:
use `pip3 install pipenv` to install on Debian/Ubuntu

1. Create a folder in the project root:
`mkdir -p shared-volumes/pg`

2. Start the environment using: `docker-compose start` from the rot folder.
Note: you can change the DB port biding to whatever is free on your system in the `.env` file in the root - see PG_PORT parameter value.

3. Apply migrations
```sh
alembic merge heads  && alembic upgrade heads
```
