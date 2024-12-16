from django.db import models

# Create your models here.

class Note(models.Model):
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)