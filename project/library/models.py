from django.contrib.auth.models import AbstractUser
from django.db import models


class LibraryUser(AbstractUser):
    USER_ROLES = (
        ('читатель', 'Читатель'), ('библиотекарь', 'Библиотекарь')
    )
    role = models.CharField(
        'Роль',
        max_length=30,
        choices=USER_ROLES,
        default=('читатель', 'Читатель')
    )
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = []


class Category(models.Model):
    name = models.CharField(
        'Название категории',
        max_length=255
    )

    def __str__(self):
        return self.name


class Book(models.Model):
    name = models.CharField(
        'Название',
        max_length=255
    )
    author_name = models.CharField(
        'Имя автора',
        max_length=255
    )
    description = models.CharField(
        'Описание',
        max_length=2000
    )
    category = models.ForeignKey(
        Category,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name
