from django.db import models


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
