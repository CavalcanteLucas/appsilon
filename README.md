# README

## Running the project

To run the project locally, you need to have docker and docker-compose installed.

Run the following command to setup the database:

```
make setup-db
```

Run the following command to run the project:

```
make run
```

The project will be available at http://localhost:8000

## Running the tests

To run the tests, run the following command:

```
make test
```

The coverage report will be available at `htmlcov/index.html`
