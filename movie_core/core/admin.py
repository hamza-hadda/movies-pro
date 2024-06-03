from django.contrib import admin

from movie_core.core.models import Actor, Movie, Review


@admin.register(Actor)
class ActorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name')


@admin.register(Movie)
class MovieAdmin(admin.ModelAdmin):
    list_display = ('title', 'description')
    filter_horizontal = ('actors',)  # Use a horizontal filter widget for the many-to-many relationship


@admin.register(Review)
class ReviewAdmin(admin.ModelAdmin):
    list_display = ('grade', 'movie')
    list_filter = ('grade', 'movie')
