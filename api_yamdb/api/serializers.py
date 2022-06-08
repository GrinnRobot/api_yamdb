import datetime as d
from rest_framework import serializers

from reviews.models import Genre, Category, Title


class CategoriesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Category
        fields = ('name', 'slug')


class GenresSerializer(serializers.ModelSerializer):

    class Meta:
        model = Genre
        fields = ('name', 'slug')


class TitlesSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True, read_only=True)
    category = CategoriesSerializer(read_only=True)

    class Meta:
        model = Title
        fields = ('__all__')

    def validate_year(self, value):
        year = d.datetime.today().year
        if year < value:
            raise serializers.ValidationError(
                'Creationyear is from future? Call the timepolice!'
            )
        return value
