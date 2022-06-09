from django.db import models


class Category(models.Model):
    name = models.CharField('Категория', max_length=256)

    slug = models.SlugField(
        unique=True,
        verbose_name='slug'
    )

    def __str__(self):
        return self.name


class Genre(models.Model):
    name = models.CharField('Жанр', max_length=256)

    slug = models.SlugField(
        unique=True,
        verbose_name='slug'
    )

    def __str__(self):
        return self.name


class Title(models.Model):
    name = models.CharField('Произведение', max_length=256)

    year = models.IntegerField('Дата выхода')

    description = models.TextField(
        'Описание',
        blank=True,
        null=True,
    )

    genre = models.ManyToManyField(
        Genre,
        verbose_name='Жанр',
        related_name='titles',
    )

    category = models.ForeignKey(
        Category,
        on_delete=models.SET_NULL,
        blank=True,
        null=True,
        related_name='titles',
        verbose_name='Категория'
    )

    def __str__(self):
        return self.name
