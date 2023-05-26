from appsilon.ext.database import db


movie_directors = db.Table(
    "movie_directors",
    db.Column(
        "movie_id",
        db.Integer,
        db.ForeignKey("movies.id"),
        primary_key=True,
    ),
    db.Column(
        "director_id",
        db.Integer,
        db.ForeignKey("directors.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)

movie_genres = db.Table(
    "movie_genres",
    db.Column(
        "movie_id",
        db.Integer,
        db.ForeignKey("movies.id"),
        primary_key=True,
    ),
    db.Column(
        "genre_id",
        db.Integer,
        db.ForeignKey("genres.id", ondelete="CASCADE"),
        primary_key=True,
    ),
)


class Movie(db.Model):
    __tablename__ = "movies"

    id = db.Column(db.Integer, primary_key=True)
    url = db.Column(db.String(255), nullable=False)
    imdb = db.Column(db.String(255), nullable=False)
    title = db.Column(db.String(255), nullable=False)
    year = db.Column(db.Integer, nullable=False)

    directors = db.relationship(
        "Director",
        secondary=movie_directors,
        backref=db.backref("movies", lazy="dynamic"),
        passive_deletes=True,
    )
    genres = db.relationship(
        "Genre",
        secondary=movie_genres,
        backref=db.backref("movies", lazy="dynamic"),
        passive_deletes=True,
    )

    def __repr__(self):
        return f"<Movie(id={self.id}, year={self.year}, url={self.url}, imdb={self.imdb}, title={self.title})>"


class Director(db.Model):
    __tablename__ = "directors"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Director(id={self.id}, name={self.name})>"


class Genre(db.Model):
    __tablename__ = "genres"

    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return f"<Genre(id={self.id}, name={self.name})>"
