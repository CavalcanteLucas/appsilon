from flask import render_template, request

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
    return render_template("index.html")


def movies():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    movies = get_movies(page=page, per_page=per_page)
    context = {
        "movies": movies.items,
        "pagination": movies,
    }
    return render_template("movies.html", **context)


def directors():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    directors = get_directors(page=page, per_page=per_page)
    context = {
        "directors": directors.items,
        "pagination": directors,
    }
    return render_template("directors.html", **context)


def genres():
    page = int(request.args.get("page", 1))
    per_page = int(request.args.get("per_page", 10))
    genres = get_genres(page=page, per_page=per_page)
    context = {
        "genres": genres.items,
        "pagination": genres,
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
