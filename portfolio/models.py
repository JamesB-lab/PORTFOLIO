from django.db import models
from django.utils.translation import gettext_lazy


class Skills(models.Model):
    python = models.BooleanField()
    excel = models.BooleanField()

class Post(models.Model):

    # class SkillTag(models.TextChoices):
    #     PYTHON = 'PYTHON', gettext_lazy('Python')
    #     EXCEL = 'EXCEL', gettext_lazy('Excel')
    #     R = 'R', gettext_lazy('R')
    #     SQL = 'SQL', gettext_lazy('SQL')
    #     AWS = 'AWS', gettext_lazy('AWS')
    #     RPI = 'RPI', gettext_lazy('Raspberry Pi')
    #     ML = 'ML', gettext_lazy('Machine Learning')
    #     DESCRIPTIVE_ANALYTICS = 'DESCRIPTIVE_ANALYTICS', gettext_lazy('Descriptive analytics')
    #     DJANGO = 'DJANGO', gettext_lazy('Django')

    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        'auth.User',
        on_delete=models.CASCADE,
    )
    body = models.TextField()
    imagePath = models.CharField(max_length=200)
    thumbnail = models.TextField()
    skills = Skills()

    def __str__(self):
        return self.title
