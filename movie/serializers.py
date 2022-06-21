from rest_framework import serializers

from .models import Movie


class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = ('imdb_id', 'title', 'released_year', 'rating', 'genre')
        read_only_fields = ['genre']

    def get_genre(self, genre):
        return genre.split(',')
