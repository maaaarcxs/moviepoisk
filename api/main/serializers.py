from moviesearch.models import Movie, Genre
from rest_framework import serializers

class GenreSerializer(serializers.Serializer):
    name = serializers.CharField()

    def create(self, validated_data):
        return Genre.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get("name", instance.name)
        instance.save()
        return instance

class MovieSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    picture = serializers.ImageField(required=False, allow_null=True)
    title = serializers.CharField()
    description = serializers.CharField(max_length=1300)
    release_date = serializers.DateField(auto_now_add=True)
    genre = serializers.PrimaryKeyRelatedField(queryset=Genre.objects.all())
    age_restriction = serializers.IntegerField()
    rating = serializers.FloatField()

    def create(self, validated_data):
        return Movie.objects.create(**validated_data)
    
    def update(self, instance, validated_data):
        instance.picture = validated_data.get("picture", instance.picture)
        instance.title = validated_data.get("title", instance.title)
        instance.description = validated_data.get("description", instance.description)
        instance.age_restriction = validated_data.get("age_restriction", instance.age_restriction)
        instance.save()
        return instance