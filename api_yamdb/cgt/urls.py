from django.urls import include, path
from rest_framework.routers import SimpleRouter

from .views import CategoriesViewSet, GenresViewSet, TitlesViewSet

app_name = 'cgt'

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

urlpatterns = [
    path('', include(router.urls)),
]
