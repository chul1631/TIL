from django.db import models
from django.forms import CharField

# Create your models here.


class Article(models.Model):
    title = models.CharField(max_length=20)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    

class Comment(models.Model):
    content = models.CharField(max_length=80)
    article = models.ForeignKey(Article, on_delete=models.CASCADE)