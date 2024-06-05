from rest_framework import serializers

from movie_core.core.models import Actor, Movie, Review


class ActorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Actor
        fields = ['id', 'first_name', 'last_name']


class ReviewSerializer(serializers.ModelSerializer):

    class Meta:
        model = Review
        fields = ['id', 'grade']


class MovieSerializer(serializers.ModelSerializer):
    actors = ActorSerializer(many=True, required=False)
    reviews = ReviewSerializer(many=True, required=False)

    class Meta:
        model = Movie
        fields = ['id', 'title', 'description', 'actors', 'reviews']

    def create(self, validated_data):
        actors_data = validated_data.pop('actors', [])
        reviews_data = validated_data.pop('reviews', [])
        movie = Movie.objects.create(**validated_data)
        for actor_data in actors_data:
            actor, created = Actor.objects.get_or_create(**actor_data)
            movie.actors.add(actor)

        for review_data in reviews_data:
            Review.objects.create(movie=movie, **review_data)
        return movie

    def update(self, instance, validated_data):
        actors_data = validated_data.pop('actors', [])
        reviews_data = validated_data.pop('reviews', [])
        instance.title = validated_data.get('title', instance.title)
        instance.description = validated_data.get('description', instance.description)
        instance.save()

        instance.actors.clear()
        instance.reviews.all().delete()

        for actor_data in actors_data:
            actor, created = Actor.objects.get_or_create(**actor_data)
            instance.actors.add(actor)
        for review_data in reviews_data:
            Review.objects.create(movie=instance, **review_data)
        return instance
