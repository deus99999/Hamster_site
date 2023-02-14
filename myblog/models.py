from django.db import models
from django.contrib.auth.models import User
from django.utils import timezone
from django.urls import reverse


class Author(models.Model):
    name = models.CharField(max_length=200)

    def get_absolute_url(self):
        return reverse('author_detail', kwargs={'pk': self.pk})


class Post(models.Model):
    title = models.CharField(max_length=200)
    url = models.SlugField()
    content = models.TextField()
    image = models.ImageField()
    created_at = models.DateField(default=timezone.now)
    author = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title