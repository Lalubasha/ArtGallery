# Generated by Django 5.0.1 on 2024-04-25 11:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GalleryApp', '0002_remove_django_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='django',
            name='image',
            field=models.ImageField(blank=True, null=True, upload_to='media/'),
        ),
    ]
