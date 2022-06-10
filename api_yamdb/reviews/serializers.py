from rest_framework import serializers
from rest_framework.validators import UniqueTogetherValidator
from .models import Review, Comment


class ReviewsSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(
        read_only=True,
        slug_field='username'
    )

    class Meta:
        model = Review
        fields = ('id', 'title', 'author', 'text', 'pub_date', 'score')
        read_only_fields = ('id', 'title', 'author', 'pub_date',)
        validators = [
            UniqueTogetherValidator(
                queryset=Review.objects.all(),
                fields=['author', 'title']
            )
        ]


class CommentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Comment
        fields = ('id', 'review', 'author', 'text', 'pub_date')
        read_only_fields = ('id', 'review', 'author', 'pub_date',)
