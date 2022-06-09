from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import (CategoriesViewSet, CommentViewSet, GenresViewSet,
                    ReviewViewSet, TitlesViewSet)

app_name = 'reviews'

router = SimpleRouter()

router.register(
    r'categories',
    CategoriesViewSet, basename='categories'
)
router.register(
    r'genres',
    GenresViewSet, basename='genres'
)
router.register(
    r'titles',
    TitlesViewSet, basename='titles'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews',
    ReviewViewSet, basename='reviews'
)
router.register(
    r'titles/(?P<title_id>\d+)/reviews/(?P<review_id>\d+)/comments',
    CommentViewSet, basename='comments',
)

urlpatterns = [
    path('', include(router.urls)),
]
