from click import echo

from appsilon.ext.database import db
from appsilon.ext.assets.wiki_data_fetcher import WikiDataFetcher
from appsilon.ext.assets.queries import Queries
from appsilon.ext.assets.transactions import (
    get_or_create_movie,
    create_movie_director,
    create_movie_genre,
)


def init_app(app):
    def create_db():
        """Create tables"""
        echo(" [x] Creating tables...")
        db.create_all()
        echo(" [x] Done!")

    def drop_db():
        """Clear existing data"""
        echo(" [x] Dropping tables...")
        db.drop_all()
        echo(" [x] Done!")

    def populate_db():
        """Populate tables with sample data"""
        echo(" [x] Loading movies into the DB...")

        fetcher = WikiDataFetcher(Queries.SELECT_MOVIES_AFTER_2013.value)
        movies = fetcher.load()

        with db.session.begin():
            for movie in movies:
                movie_instance = get_or_create_movie(movie)
                if movie_instance:
                    if "director" in movie:
                        create_movie_director(
                            movie_instance,
                            director_name=movie["directorLabel"],
                        )

                    if "genre" in movie:
                        create_movie_genre(
                            movie_instance,
                            genre_name=movie["genreLabel"],
                        )

        echo(f" [x] Done!")

    for command in [
        create_db,
        drop_db,
        populate_db,
    ]:
        app.cli.add_command(app.cli.command()(command))
