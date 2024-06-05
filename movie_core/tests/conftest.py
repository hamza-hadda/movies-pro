import pytest

from rest_framework.test import APIClient

from movie_core.core.models import Actor


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def actor_data():
    return [
        {"first_name": "John", "last_name": "Doe"},
        {"first_name": "Jane", "last_name": "Smith"},
    ]

@pytest.fixture
def create_actors(db, actor_data):
    return [Actor.objects.create(**actor) for actor in actor_data]

@pytest.fixture
def movie_data(actor_data):
    return [
        {"title": "Movie 1", "description": "Description of Movie 1"},
        {"title": "Movie 2", "description": "Description of Movie 2"},
    ]


@pytest.fixture
def review_data(movie_data):
    return [
        {"grade": 5},
        {"grade": 3},
    ]
