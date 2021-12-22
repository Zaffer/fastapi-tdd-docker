# Test-Driven Development with FastAPI and Docker

![Continuous Integration and Delivery](https://github.com/Zaffer/fastapi-tdd-docker/workflows/Continuous%20Integration%20and%20Delivery/badge.svg?branch=master)


# Dev
`uvicorn app.main:app --reload`


# Build
`docker-compose build`


# Run
`docker-compose up -d`


# Database
`docker-compose exec web-db psql -U postgres`
`\c web_dev`
`\q`


# Pytest Commands
Let's review some useful pytest commands:

## build the container first
`docker-compose up -d --build`


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


## Testing
```
docker-compose up -d --build
```
```
docker-compose exec web python -m pytest
```
```
docker-compose exec web python -m pytest --cov="." --cov-report html
```
```
docker-compose exec web pytest -k "unit" -n auto
```

## Quality
```
docker-compose up -d --build
```
```
docker-compose exec web flake8 .
docker-compose exec web black . --check
docker-compose exec web isort . --check-only
```

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

## COMMANDS:
$ docker-compose down -v
$ docker-compose up -d --build
$ docker-compose exec web aerich upgrade

$ docker-compose exec web python -m pytest
$ docker-compose exec web flake8 .
$ docker-compose exec web black .
$ docker-compose exec web isort .