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
    assert len(response.json()) > 0  # Assuming there are movies in the database

