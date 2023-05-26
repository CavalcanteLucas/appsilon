from flask import render_template

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
)


def index():
    context = {
        "movies": get_movies(),
        "directors": get_directors(),
        "genres": get_genres(),
    }
    return render_template("index.html", **context)


def movies():
    context = {
        "movies": get_movies(),
    }
    return render_template("movies.html", **context)


def directors():
    context = {
        "directors": get_directors(),
    }
    return render_template("directors.html", **context)


def genres():
    context = {
        "genres": get_genres(),
    }
    return render_template("genres.html", **context)


def movies_by_director(director_id):
    context = {
        "director": get_director_by_id(director_id),
        "movies": get_movies_by_director(director_id),
    }
    return render_template("movies_by_director.html", **context)


def movies_by_genre(genre_id):
    context = {
        "genre": get_genre_by_id(genre_id),
        "movies": get_movies_by_genre(genre_id),
    }
    return render_template("movies_by_genre.html", **context)


def movie_details(movie_id):
    context = {
        "movie": get_movie_by_id(movie_id),
        "genres": get_genres_by_movie(movie_id),
        "directors": get_directors_by_movie(movie_id),
    }
    return render_template("movie_details.html", **context)
