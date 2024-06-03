from django.db import models


class Actor(models.Model):
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Movie(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    actors = models.ManyToManyField(Actor, related_name="actor_movies")

    def __str__(self):
        return self.title


class Review(models.Model):
    grade = models.IntegerField()
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name="reviews")

    def __str__(self):
        return f"Review for {self.movie.title} with grade {self.grade}"

    def save(self, *args, **kwargs):
        if not 1 <= self.grade <= 5:
            raise ValueError("Grade must be between 1 and 5.")
        super().save(*args, **kwargs)