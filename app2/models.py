from django.db import models

# Create your models here.
class DecryptedNote(models.Model):
    decrypted_content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)