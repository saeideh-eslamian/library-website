from django.contrib import admin
from .models import Book, Author, User, Comment

admin.site.register(Book)
admin.site.register(Author)
admin.site.register(User)
admin.site.register(Comment)
