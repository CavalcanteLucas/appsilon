from flask import Blueprint

from appsilon.blueprints.views.routes import (
    index,
    movies,
    directors,
    genres,
    movies_by_director,
    movies_by_genre,
    movie_details,
)

bp = Blueprint("views", __name__, template_folder="templates")

bp.add_url_rule("/", view_func=index)
bp.add_url_rule("/movies", view_func=movies)
bp.add_url_rule("/directors", view_func=directors)
bp.add_url_rule("/genres", view_func=genres)
bp.add_url_rule("/movies_by_director/<int:director_id>", view_func=movies_by_director)
bp.add_url_rule("/movies_by_genre/<int:genre_id>", view_func=movies_by_genre)
bp.add_url_rule("/movie_details/<int:movie_id>", view_func=movie_details)


def init_app(app):
    app.register_blueprint(bp)
