# Generated by Django 3.1.14 on 2023-02-22 23:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_post_skill_six_sigma'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='active',
            field=models.BooleanField(default=True, editable=False),
        ),
    ]
