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


class TitlesGetSerializer(serializers.ModelSerializer):
    genre = GenresSerializer(many=True, read_only=True)
    category = CategoriesSerializer(read_only=True)
    rating = serializers.SerializerMethodField()

    class Meta:
        model = Title
        fields = (
            'id', 'name', 'year', 'rating',
            'description', 'genre', 'category',
        )

    def get_rating(self):
        return 5

    def validate_year(self, value):
        year = d.datetime.today().year
        if year < value:
            raise serializers.ValidationError(
                'Creationyear is from future? Call the timepolice!'
            )
        return value


class TitlesPostSerializer(serializers.ModelSerializer):
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        slug_field='slug'
    )
    genre = serializers.SlugRelatedField(
        queryset=Genre.objects.all(),
        slug_field='slug',
        many=True
    )

    class Meta:
        fields = '__all__'
        model = Title

    def validate_year(self, value):
        year = d.datetime.today().year
        if year < value:
            raise serializers.ValidationError(
                'Creationyear is from future? Call the timepolice!'
            )
        return value
