# Generated by Django 3.1.14 on 2023-02-22 20:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0002_post_imagepath'),
    ]

    operations = [
        migrations.AlterField(
            model_name='post',
            name='imagePath',
            field=models.CharField(max_length=200),
        ),
    ]
