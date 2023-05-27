# APPSILON

Discover the Cinematic Universe: Explore Movies, Directors, and Genres on IMDb

## Running the project

### Locally

To run the project locally, you'll need to have Python3 installed. Make sure to create an isolated virtual environment and activate it. Install the dependencies:
```
pip install -r requirements.txt
```

You'll also need an instance of PostgreSQL running locally. Setup the credentials in the `.env` file (see `.example.env`).

Then, setup the database and run the application:
```
make setup-db
make run
```

The project will be available at http://localhost:8000.


### Docker

To run the project locally using Docker, you need to have `Docker` and `docker-compose` installed.

If that's the first time you're running the application, execute the following command to setup the database and run the application:
```
make docker-setup-db-and-run
```

Otherwise, just run the following command:
```
make run
```

The project will be available at http://localhost:8000.

## Running the tests

To run the tests, run the following command:

```
make test
```

The coverage report will be available at `htmlcov/index.html`

# Author

Designed and developed by [Lucas Cavalcante](https://github.com/CavalcanteLucas).
