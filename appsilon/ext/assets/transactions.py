from appsilon.ext.database import db
from appsilon.models import (
    Movie,
    Director,
    Genre,
    movie_directors,
    movie_genres,
)


def get_movies():
    return Movie.query.all()


def get_directors():
    return Director.query.all()


def get_genres():
    return Genre.query.all()


def get_movie_by_id(movie_id):
    return Movie.query.get(movie_id)


def get_director_by_id(director_id):
    return Director.query.get(director_id)


def get_genre_by_id(genre_id):
    return Genre.query.get(genre_id)


def get_movies_by_director(director_id):
    movies_by_director = db.session.query(movie_directors).filter_by(director_id=director_id).all()
    movies = []
    for movie_by_director in movies_by_director:
        movie = Movie.query.get(movie_by_director.movie_id)
        movies.append(movie)
    return movies


def get_movies_by_genre(genre_id):
    movies_by_genre = db.session.query(movie_genres).filter_by(genre_id=genre_id).all()
    movies = []
    for movie_by_genre in movies_by_genre:
        movie = Movie.query.get(movie_by_genre.movie_id)
        movies.append(movie)
    return movies


def get_genres_by_movie(movie_id):
    genres_by_movie = db.session.query(movie_genres).filter_by(movie_id=movie_id).all()
    genres = []
    for genre_by_movie in genres_by_movie:
        genre = Genre.query.get(genre_by_movie.genre_id)
        genres.append(genre)
    return genres


def get_directors_by_movie(movie_id):
    directors_by_movie = db.session.query(movie_directors).filter_by(movie_id=movie_id).all()
    directors = []
    for director_by_movie in directors_by_movie:
        director = Director.query.get(director_by_movie.director_id)
        directors.append(director)
    return directors


def get_or_create_movie(movie_data):
    movie_url = movie_data["movie"]
    movie_imdb = movie_data["imdbId"]
    movie_title = movie_data["movieLabel"]

    movie_instance = Movie.query.filter_by(url=movie_url, imdb=movie_imdb, title=movie_title).first()
    if not movie_instance:
        movie_instance = Movie(url=movie_url, imdb=movie_imdb, title=movie_title)
        db.session.add(movie_instance)
        db.session.flush()

    return movie_instance


def get_or_create_director(director_name):
    director_instance = Director.query.filter_by(name=director_name).first()
    if not director_instance:
        director_instance = Director(name=director_name)
        db.session.add(director_instance)
        db.session.flush()

    return director_instance


def get_or_create_genre(genre_name):
    genre_instance = Genre.query.filter_by(name=genre_name).first()
    if not genre_instance:
        genre_instance = Genre(name=genre_name)
        db.session.add(genre_instance)
        db.session.flush()

    return genre_instance


def create_movie_director(movie_instance, director_name):
    director_instance = get_or_create_director(director_name)

    movie_director_instance = (
        db.session.query(movie_directors)
        .filter_by(
            movie_id=movie_instance.id,
            director_id=director_instance.id,
        )
        .first()
    )
    if not movie_director_instance:
        db.session.execute(
            movie_directors.insert().values(
                movie_id=movie_instance.id,
                director_id=director_instance.id,
            )
        )
        db.session.flush()


def create_movie_genre(movie_instance, genre_name):
    genre_instance = get_or_create_genre(genre_name)

    movie_genre_instance = (
        db.session.query(movie_genres)
        .filter_by(
            movie_id=movie_instance.id,
            genre_id=genre_instance.id,
        )
        .first()
    )
    if not movie_genre_instance:
        db.session.execute(
            movie_genres.insert().values(
                movie_id=movie_instance.id,
                genre_id=genre_instance.id,
            )
        )
        db.session.flush()
