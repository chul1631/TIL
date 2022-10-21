from django.db import models

# Create your models here.
class App(models.Model):
    title = models.CharField(max_length=20)
    summary = models.CharField(max_length=500)
    runningtime = models.DateField(null=True)
