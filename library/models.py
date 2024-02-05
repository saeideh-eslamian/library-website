from django.db import models
from django.utils.text import slugify


class Author(models.Model):
    name = models.CharField(max_length=200)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    about = models.TextField(blank=True)

    def __str__(self) -> str:
        return self.name


class User(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()
    phone = models.CharField(max_length=15)

    def __str__(self) -> str:
        return self.name


class Comment(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_published = models.DateTimeField(auto_now_add=True)

    def __str__(self) -> str:
        return f'{self.title}  {self.date_published}'


class Book(models.Model):
    title = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(null=False, unique=True)
    image = models.ImageField(upload_to='images', null=True, blank=True)
    author = models.ForeignKey(Author, on_delete=models.SET_NULL, null=True)
    stock = models.IntegerField(default=0)
    rating = models.IntegerField(null=True, blank=True)
    description = models.TextField(null=True, blank=True)
    comment = models.ForeignKey(
        Comment, on_delete=models.CASCADE, null=True, blank=True)

    def save(self, *args, **kwargs):
        if not self.id:  # Check if the object is being created for the first time
            self.slug = slugify(self.title)
        super().save(*args, **kwargs)

    def __str__(self) -> str:
        return f'{self.title}: {self.author} ==> stock: {self.stock} '
