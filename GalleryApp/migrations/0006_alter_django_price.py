# Generated by Django 5.0.1 on 2024-04-25 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('GalleryApp', '0005_django_price_alter_django_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='django',
            name='price',
            field=models.FloatField(),
        ),
    ]
