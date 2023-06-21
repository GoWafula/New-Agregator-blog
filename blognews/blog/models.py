from django.db import models
from django.utils import timezone

# Create your models here.

def get_default_date():
    return timezone.now().date().strftime('%Y-%m-%d')


class Article(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=100, blank=True)
    pub_date = models.DateField(default=get_default_date)
    url = models.URLField(unique=True)


    def __str__(self):
        return self.title