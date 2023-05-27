from appsilon.ext.database import db
from appsilon.models import (
    Movie,
    Director,
    Genre,
    movie_directors,
    movie_genres,
)
from appsilon.ext.assets.transactions import (
    get_movies,
    get_directors,
    get_genres,
    get_movie_by_id,
    get_director_by_id,
    get_genre_by_id,
    get_genres_by_movie,
    get_directors_by_movie,
    get_movies_by_director,
    get_movies_by_genre,
    get_or_create_director,
    get_or_create_genre,
    get_or_create_movie,
    create_movie_director,
    create_movie_genre,
)


def test_get_movie_by_id(app):
    with app.app_context():
        movie = Movie(
            title="My Movie",
            year=2023,
            url="https://www.example.com/movie",
            imdb="tt1234567",
        )
        db.session.add(movie)
        db.session.commit()

        retrieved_movie = get_movie_by_id(movie.id)
        assert retrieved_movie.title == "My Movie"
        assert retrieved_movie.year == 2023
        assert retrieved_movie.url == "https://www.example.com/movie"
        assert retrieved_movie.imdb == "tt1234567"


def test_get_director_by_id(app):
    with app.app_context():
        director = Director(
            name="My Director",
        )
        db.session.add(director)
        db.session.commit()

        retrieved_director = get_director_by_id(director.id)
        assert retrieved_director.name == "My Director"


def test_get_genre_by_id(app):
    with app.app_context():
        genre = Genre(
            name="My Genre",
        )
        db.session.add(genre)
        db.session.commit()

        retrieved_genre = get_genre_by_id(genre.id)
        assert retrieved_genre.name == "My Genre"


def test_get_movies_returns_paginated_list(app):
    with app.app_context():
        for i in range(20):
            db.session.add(
                Movie(
                    title=f"My Movie {i}",
                    year=2000,
                    url="https://www.example.com/movie/{i}",
                    imdb=f"zz0000{i}",
                )
            )
        db.session.commit()

        assert len(get_movies().items) == 10
        assert len(get_movies(page=2).items) == 10


def test_get_directors_returns_paginated_list(app):
    with app.app_context():
        for i in range(20):
            db.session.add(
                Director(
                    name=f"My Director {i}",
                )
            )
        db.session.commit()

    assert len(get_directors().items) == 10
    assert len(get_directors(page=2).items) == 10


def test_get_genres_returns_paginated_list(app):
    with app.app_context():
        for i in range(20):
            db.session.add(
                Genre(
                    name=f"My Genre {i}",
                )
            )
        db.session.commit()

    assert len(get_genres().items) == 10
    assert len(get_genres(page=2).items) == 10


def test_get_movies_by_director(app):
    with app.app_context():
        director = Director(name="My Director")
        db.session.add(director)

        movie1 = Movie(
            title="My Movie 1",
            year=2023,
            url="https://www.example.com/movie/1",
            imdb="tt1234561",
        )
        movie2 = Movie(
            title="My Movie 2",
            year=2023,
            url="https://www.example.com/movie/2",
            imdb="tt1234562",
        )

        db.session.add(movie1)
        db.session.add(movie2)

        db.session.commit()

        db.session.execute(
            movie_directors.insert().values(
                movie_id=movie1.id,
                director_id=director.id,
            )
        )
        db.session.execute(
            movie_directors.insert().values(
                movie_id=movie2.id,
                director_id=director.id,
            )
        )

        movies = get_movies_by_director(director.id)
        assert len(movies) == 2
        assert movies[0].title == "My Movie 1"
        assert movies[1].title == "My Movie 2"


def test_get_movie_by_genre(app):
    with app.app_context():
        genre = Genre(name="My Genre")
        db.session.add(genre)

        movie1 = Movie(
            title="My Movie 1",
            year=2023,
            url="https://www.example.com/movie/1",
            imdb="tt1234561",
        )
        movie2 = Movie(
            title="My Movie 2",
            year=2023,
            url="https://www.example.com/movie/2",
            imdb="tt1234562",
        )

        db.session.add(movie1)
        db.session.add(movie2)

        db.session.commit()

        db.session.execute(
            movie_genres.insert().values(
                movie_id=movie1.id,
                genre_id=genre.id,
            )
        )
        db.session.execute(
            movie_genres.insert().values(
                movie_id=movie2.id,
                genre_id=genre.id,
            )
        )

        movies = get_movies_by_genre(genre.id)
        assert len(movies) == 2
        assert movies[0].title == "My Movie 1"
        assert movies[1].title == "My Movie 2"


def test_get_directors_by_movie(app):
    with app.app_context():
        director1 = Director(name="My Director 1")
        director2 = Director(name="My Director 2")
        db.session.add(director1)
        db.session.add(director2)

        movie = Movie(
            title="My Movie",
            year=2023,
            url="https://www.example.com/movie",
            imdb="tt1234567",
        )
        db.session.add(movie)

        db.session.commit()

        db.session.execute(
            movie_directors.insert().values(
                movie_id=movie.id,
                director_id=director1.id,
            )
        )
        db.session.execute(
            movie_directors.insert().values(
                movie_id=movie.id,
                director_id=director2.id,
            )
        )

        directors = get_directors_by_movie(movie.id)
        assert len(directors) == 2
        assert directors[0].name == "My Director 1"
        assert directors[1].name == "My Director 2"


def test_get_genres_by_movie(app):
    with app.app_context():
        genre1 = Genre(name="My Genre 1")
        genre2 = Genre(name="My Genre 2")
        db.session.add(genre1)
        db.session.add(genre2)

        movie = Movie(
            title="My Movie",
            year=2023,
            url="https://www.example.com/movie",
            imdb="tt1234567",
        )
        db.session.add(movie)

        db.session.commit()

        db.session.execute(
            movie_genres.insert().values(
                movie_id=movie.id,
                genre_id=genre1.id,
            )
        )
        db.session.execute(
            movie_genres.insert().values(
                movie_id=movie.id,
                genre_id=genre2.id,
            )
        )

        genres = get_genres_by_movie(movie.id)
        assert len(genres) == 2
        assert genres[0].name == "My Genre 1"
        assert genres[1].name == "My Genre 2"


def test_get_or_create_movie_when_movie_exists(app):
    with app.app_context():
        movie_data = {
            "movie": "https://www.example.com/movie",
            "imdbId": "tt1234567",
            "movieLabel": "My Movie",
            "publicationYear": 2023,
        }

        movie_instance = get_or_create_movie(movie_data)
        assert isinstance(movie_instance, Movie)
        assert movie_instance.url == "https://www.example.com/movie"
        assert movie_instance.imdb == "tt1234567"
        assert movie_instance.title == "My Movie"
        assert movie_instance.year == 2023

        duplicate_instance = get_or_create_movie(movie_data)
        assert movie_instance.id == duplicate_instance.id


def test_get_or_create_movie_when_movie_does_not_exist(app):
    with app.app_context():
        movie_data = {
            "movie": "https://www.example.com/nonexistent_movie",
            "imdbId": "tt9999999",
            "movieLabel": "Nonexistent Movie",
            "publicationYear": 2023,
        }

        movie_query = Movie.query.filter_by(url=movie_data["movie"]).first()
        assert movie_query is None

        movie_instance = get_or_create_movie(movie_data)

        assert isinstance(movie_instance, Movie)
        assert movie_instance.url == "https://www.example.com/nonexistent_movie"
        assert movie_instance.imdb == "tt9999999"
        assert movie_instance.title == "Nonexistent Movie"
        assert movie_instance.year == 2023

        movie_query = Movie.query.filter_by(url=movie_data["movie"]).first()
        assert movie_query is not None
        assert movie_query.id == movie_instance.id


def test_get_or_create_director_when_director_exists(app):
    with app.app_context():
        director_name = "My Director"

        director_instance = get_or_create_director(director_name)
        assert isinstance(director_instance, Director)
        assert director_instance.name == "My Director"

        duplicate_instance = get_or_create_director(director_name)
        assert director_instance.id == duplicate_instance.id


def test_get_or_create_director_when_director_does_not_exist(app):
    with app.app_context():
        director_name = "Nonexistent Director"

        director_query = Director.query.filter_by(name=director_name).first()
        assert director_query is None

        director_instance = get_or_create_director(director_name)

        assert isinstance(director_instance, Director)
        assert director_instance.name == "Nonexistent Director"

        director_query = Director.query.filter_by(name=director_name).first()
        assert director_query is not None
        assert director_query.id == director_instance.id


def test_get_or_create_genre_when_genre_exists(app):
    with app.app_context():
        genre_name = "My Genre"

        genre_instance = get_or_create_genre(genre_name)
        assert isinstance(genre_instance, Genre)
        assert genre_instance.name == "My Genre"

        duplicate_instance = get_or_create_genre(genre_name)
        assert genre_instance.id == duplicate_instance.id


def test_get_or_create_genre_when_genre_does_not_exist(app):
    with app.app_context():
        genre_name = "Nonexistent Genre"

        genre_query = Genre.query.filter_by(name=genre_name).first()
        assert genre_query is None

        genre_instance = get_or_create_genre(genre_name)

        assert isinstance(genre_instance, Genre)
        assert genre_instance.name == "Nonexistent Genre"

        genre_query = Genre.query.filter_by(name=genre_name).first()
        assert genre_query is not None
        assert genre_query.id == genre_instance.id


def test_create_movie_director(app):
    with app.app_context():
        movie = Movie(
            title="My Movie",
            year=2023,
            url="https://www.example.com/movie",
            imdb="tt1234567",
        )
        db.session.add(movie)
        db.session.commit()

        director = Director(name="My Director")
        db.session.add(director)

        create_movie_director(movie, director.name)

        movie_directors_query = db.session.query(movie_directors).filter_by(movie_id=movie.id).all()
        assert len(movie_directors_query) == 1


def test_create_movie_genre(app):
    with app.app_context():
        movie = Movie(
            title="My Movie",
            year=2023,
            url="https://www.example.com/movie",
            imdb="tt1234567",
        )
        db.session.add(movie)
        db.session.commit()

        genre = Genre(name="My Genre")
        db.session.add(genre)

        create_movie_genre(movie, genre.name)

        movie_genres_query = db.session.query(movie_genres).filter_by(movie_id=movie.id).all()
        assert len(movie_genres_query) == 1
