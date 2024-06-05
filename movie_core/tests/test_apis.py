# myapp/tests/test_views.py
import pytest
from django.urls import reverse
from rest_framework import status

from movie_core.core.models import Movie


@pytest.mark.django_db
def test_movie_list(api_client, movie_data):
    Movie.objects.create(**movie_data[0])

    url = reverse('movie-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.json()["count"] == 1


@pytest.mark.django_db
def test_create_movie_with_actors(api_client, actor_data):
    url = reverse('movie-list')
    data = {
        "title": "New Movie",
        "description": "A description of the new movie.",
        "actors": actor_data
    }
    response = api_client.post(url, data, format='json')
    assert response.status_code == status.HTTP_201_CREATED
    movie = Movie.objects.get(id=response.data['id'])
    assert movie.title == "New Movie"
    assert movie.description == "A description of the new movie."
    assert len(movie.actors.all()) == 2


@pytest.mark.django_db
def test_update_movie_with_actors(api_client, actor_data, create_actors):
    movie = Movie.objects.create(title="Old Movie", description="An old movie.")
    movie.actors.set(create_actors[:1])

    url = reverse('movie-detail', args=[movie.id])
    data = {
        "title": "Updated Movie",
        "description": "An updated description.",
        "actors": actor_data
    }
    response = api_client.put(url, data, format='json')
    assert response.status_code == status.HTTP_200_OK
    movie.refresh_from_db()
    assert movie.title == "Updated Movie"
    assert movie.description == "An updated description."
    assert len(movie.actors.all()) == 2

