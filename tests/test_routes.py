def test_request_returns_404(client):
    assert client.get("/url_that_does_not_exist").status_code == 404


def test_request_returns_200(client):
    assert client.get("/").status_code == 200


def test_request_returns_200_for_movies(client):
    assert client.get("/movies").status_code == 200


def test_request_returns_200_for_directors(client):
    assert client.get("/directors").status_code == 200


def test_request_returns_200_for_genres(client):
    assert client.get("/genres").status_code == 200


def test_request_returns_200_for_movies_by_director(client):
    assert client.get("/movies_by_director/1").status_code == 200


def test_request_returns_200_for_movies_by_genre(client):
    assert client.get("/movies_by_genre/1").status_code == 200


def test_request_returns_200_for_movie_details(client):
    assert client.get("/movie_details/1").status_code == 200
