from django.core.management.base import BaseCommand
from django.core.management import call_command

from movie_core.core.models import Actor, Movie, Review


class Command(BaseCommand):
    help = 'Load initial fixtures if the database is empty'

    def handle(self, *args, **options):
        if not Actor.objects.exists() and not Movie.objects.exists() and not Review.objects.exists():
            self.stdout.write(self.style.SUCCESS('Database is empty, loading fixtures...'))
            call_command('loaddata', 'movie_core/core/fixtures/actors.json', verbosity=0)
            call_command('loaddata', 'movie_core/core/fixtures/movies.json', verbosity=0)
            call_command('loaddata', 'movie_core/core/fixtures/reviews.json', verbosity=0)
            self.stdout.write(self.style.SUCCESS('Fixtures loaded successfully.'))
        else:
            self.stdout.write(self.style.SUCCESS('Database is not empty, skipping fixture loading.'))
