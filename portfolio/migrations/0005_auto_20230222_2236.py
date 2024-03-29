# Generated by Django 3.1.14 on 2023-02-22 22:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0004_post_thumbnail'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='skill_aws',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='skill_descriptive_analytics',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='skill_excel',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='skill_machine_learning',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='skill_python',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='skill_r',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='skill_raspberry_pi',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='post',
            name='skill_sql',
            field=models.BooleanField(default=False),
        ),
    ]
