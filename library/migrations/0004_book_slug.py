# Generated by Django 5.0.1 on 2024-02-05 13:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('library', '0003_author_image_book_image_alter_book_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='slug',
            field=models.SlugField(null=True, unique=True),
        ),
    ]
