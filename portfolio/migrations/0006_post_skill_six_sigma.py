# Generated by Django 3.1.14 on 2023-02-22 23:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_auto_20230222_2236'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='skill_six_sigma',
            field=models.BooleanField(default=False),
        ),
    ]
