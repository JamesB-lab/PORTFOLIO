from django.db import models
from django.utils.timezone import now


class Post(models.Model):

    # Only active posts will be shown
    active = models.BooleanField(default=True)

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    created_at = models.DateTimeField(default=now())
    body = models.TextField()
    imagePath = models.CharField(max_length=200)
    thumbnail = models.TextField()
    
    # Skills
    skill_python = models.BooleanField(default=False)
    skill_excel = models.BooleanField(default=False)
    skill_r = models.BooleanField(default=False)
    skill_sql = models.BooleanField(default=False)
    skill_aws = models.BooleanField(default=False)
    skill_raspberry_pi = models.BooleanField(default=False)
    skill_machine_learning = models.BooleanField(default=False)
    skill_descriptive_analytics = models.BooleanField(default=False)
    skill_six_sigma = models.BooleanField(default=False)

    def __str__(self):
        return self.title

    # Prevents permanent deletion by setting active to False instead
    def delete(self):
        self.active = False
        self.save()
