from django.shortcuts import get_object_or_404

from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated, AllowAny

from .models import Review, Title
from .serializers import ReviewsSerializer, CommentsSerializer
from .permissions import IsStaffOrAuthorOrReadOnly


class ReviewsViewSet(viewsets.ModelViewSet):
    serializer_class = ReviewsSerializer

    def perform_create(self, serializer):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        serializer.save(title=title, author=self.request.user)

    def get_queryset(self):
        title_id = self.kwargs.get('title_id')
        title = get_object_or_404(Title, pk=title_id)
        return title.reviews.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = [AllowAny]
        elif self.action == 'post':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsStaffOrAuthorOrReadOnly]
        return [permission() for permission in permission_classes]


class CommentsViewSet(viewsets.ModelViewSet):
    serializer_class = CommentsSerializer

    def perform_create(self, serializer):
        review_id = self.kwargs.get('review_id')
        # review = get_object_or_404(Review, pk=review_id)
        serializer.data['author'] = self.request.user
        serializer.data['review'] = get_object_or_404(Review, pk=review_id)
        serializer.is_valid(raise_exception=True)
        serializer.save()

    def get_queryset(self):
        review_id = self.kwargs.get('review_id')
        review = get_object_or_404(Review, pk=review_id)
        return review.comments.all()

    def get_permissions(self):
        if self.action in ('list', 'retrieve'):
            permission_classes = [AllowAny]
        elif self.action == 'post':
            permission_classes = [IsAuthenticated]
        else:
            permission_classes = [IsStaffOrAuthorOrReadOnly]
        return [permission() for permission in permission_classes]
