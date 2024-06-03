# tests/test_models.py
import pytest

from movie_core.core.models import Actor, Movie, Review


@pytest.mark.django_db
def test_create_actor(actor_data):
    actor = Actor.objects.create(**actor_data[0])
    assert Actor.objects.count() == 1


@pytest.mark.django_db
def test_create_movie(movie_data):
    movie = Movie.objects.create(**movie_data[0])
    assert Movie.objects.count() == 1


@pytest.mark.django_db
def test_create_review(review_data, movie_data):
    movie = Movie.objects.create(**movie_data[0])
    review = Review.objects.create(movie=movie, **review_data[0])
    assert Review.objects.count() == 1
