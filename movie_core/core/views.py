from rest_framework import viewsets, mixins

from movie_core.core.models import Actor, Movie, Review
from movie_core.core.serializers import ActorSerializer, MovieSerializer, ReviewSerializer


class ActorViewSet(
    mixins.CreateModelMixin,
    mixins.RetrieveModelMixin,
    mixins.UpdateModelMixin,
    mixins.DestroyModelMixin,
    mixins.ListModelMixin,
    viewsets.GenericViewSet
    ):
    queryset = Actor.objects.all()
    serializer_class = ActorSerializer

class MovieViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   viewsets.GenericViewSet):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer

class ReviewViewSet(mixins.CreateModelMixin,
                    mixins.RetrieveModelMixin,
                    mixins.UpdateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Review.objects.all()
    serializer_class = ReviewSerializer
