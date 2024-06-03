from django.urls import path, include
from rest_framework.routers import DefaultRouter

from movie_core.core.views import ActorViewSet, MovieViewSet, ReviewViewSet

router = DefaultRouter()
router.register(r'actors', ActorViewSet)
router.register(r'movies', MovieViewSet)
router.register(r'reviews', ReviewViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
