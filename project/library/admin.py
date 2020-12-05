from django.contrib import admin

from library.models import Book, Category, LibraryUser

admin.site.register(Book)
admin.site.register(Category)
admin.site.register(LibraryUser)
