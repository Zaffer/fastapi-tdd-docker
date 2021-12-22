# Test-Driven Development with FastAPI and Docker

![Continuous Integration and Delivery](https://github.com/Zaffer/fastapi-tdd-docker/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)


# Pytest Commands
Let's review some useful pytest commands:

## normal run
`$ docker-compose exec web python -m pytest`

## disable warnings
`$ docker-compose exec web python -m pytest -p no:warnings`

## run only the last failed tests
`$ docker-compose exec web python -m pytest --lf`

## run only the tests with names that match the string expression
`$ docker-compose exec web python -m pytest -k "summary and not test_read_summary"`

## stop the test session after the first failure
```$ docker-compose exec web python -m pytest -x```

## enter PDB after first failure then end the test session
`$ docker-compose exec web python -m pytest -x --pdb`

## stop the test run after two failures
`$ docker-compose exec web python -m pytest --maxfail=2`

## show local variables in tracebacks
`$ docker-compose exec web python -m pytest -l`

## list the 2 slowest tests
`$ docker-compose exec web python -m pytest --durations=2`


## Run the tests with coverage:
`$ docker-compose exec web python -m pytest --cov="."`



## Github Actions
`
docker build -f project/Dockerfile.prod -t docker.pkg.github.com/zaffer/fastapi-tdd-docker/summarizer:latest ./project
`
`
docker login docker.pkg.github.com -u <USERNAME> -p <TOKEN>
`
`
docker push docker.pkg.github.com/zaffer/fastapi-tdd-docker/summarizer:latest
`

## Common Commands
Build the images:
`$ docker-compose build`

Run the containers:
`$ docker-compose up -d`

Apply the migrations:
```
$ docker-compose exec web aerich upgrade

# prefer just to apply the latest changes to the database, without the migrations?
# $ docker-compose exec web python app/db.py
```

Run the tests:
`$ docker-compose exec web python -m pytest`

Run the tests with coverage:
`$ docker-compose exec web python -m pytest --cov="."`

Lint:
`$ docker-compose exec web flake8 .`

Run Black and isort with check options:
```
$ docker-compose exec web black . --check
$ docker-compose exec web isort . --check-only
```

Make code changes with Black and isort:
```
$ docker-compose exec web black .
$ docker-compose exec web isort .
```

`docker build --no-cache -f project/Dockerfile.prod -t web ./project `
`docker run --name fastapi-tdd -e PORT=8765 -e DATABASE_URL=sqlite://sqlite.db -p 5003:8765 web:latest`

# Other Commands
To stop the containers:
`$ docker-compose stop`

To bring down the containers:
`$ docker-compose down`

Want to force a build?
`$ docker-compose build --no-cache`

Remove images:
`$ docker rmi $(docker images -q)`

# Postgres
Want to access the database via psql?
`$ docker-compose exec web-db psql -U postgres`

Then, you can connect to the database and run SQL queries. For example:
```
# \c web_dev
# select * from textsummary;
```