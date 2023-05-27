from appsilon.models import (
    Movie,
    Director,
    Genre,
)


def test_movie_model():
    movie = Movie(
        url="https://www.example.com/movie",
        imdb="tt1234567",
        title="Test Movie",
        year=2021,
    )

    assert movie.url == "https://www.example.com/movie"
    assert movie.imdb == "tt1234567"
    assert movie.title == "Test Movie"
    assert movie.year == 2021

    assert (
        repr(movie)
        == "<Movie(id=None, year=2021, url=https://www.example.com/movie, imdb=tt1234567, title=Test Movie)>"
    )


def test_director_model():
    director = Director(name="Test Director")

    assert director.name == "Test Director"

    assert repr(director) == "<Director(id=None, name=Test Director)>"


def test_genre_model():
    genre = Genre(name="Test Genre")

    assert genre.name == "Test Genre"

    assert repr(genre) == "<Genre(id=None, name=Test Genre)>"
