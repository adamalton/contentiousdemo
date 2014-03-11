from django.db import models

class TextString(models.Model):
    label = models.CharField(max_length=100)
    text = models.CharField(max_length=255, blank=True)

