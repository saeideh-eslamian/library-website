from django.contrib import admin
from .models import Book, Author, User, Comment

class BookAdmin(admin.ModelAdmin):
    list_display = ('title','author','stock')
    list_filter = ('author','rating')
    search_fields = ('title','description','author')
    prepopulated_fields ={'slug': ('title', )}


class AuthorAdmin(admin.ModelAdmin):
    list_display = ('name',)

admin.site.register(Book,BookAdmin)
admin.site.register(Author, AuthorAdmin)
admin.site.register(User)
admin.site.register(Comment)
