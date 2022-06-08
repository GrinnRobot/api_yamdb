from rest_framework import viewsets, mixins, filters

from reviews.models import Category, Genre, Title
from .permissions import IsMyAdminOrReadOnly
from .serializers import (CategoriesSerializer, GenresSerializer,
                          TitlesSerializer)


class CategoriesViewSet(mixins.CreateModelMixin,
                        mixins.DestroyModelMixin,
                        mixins.ListModelMixin,
                        viewsets.GenericViewSet):
    queryset = Category.objects.all()
    serializer_class = CategoriesSerializer
    permission_classes = (IsMyAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class GenresViewSet(mixins.CreateModelMixin,
                    mixins.DestroyModelMixin,
                    mixins.ListModelMixin,
                    viewsets.GenericViewSet):
    queryset = Genre.objects.all()
    serializer_class = GenresSerializer
    permission_classes = (IsMyAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)
    lookup_field = 'slug'


class TitlesViewSet(viewsets.ModelViewSet):
    queryset = Title.objects.all()
    serializer_class = TitlesSerializer
    permission_classes = (IsMyAdminOrReadOnly,)
    filter_backends = (filters.SearchFilter,)
    search_fields = ('name',)

