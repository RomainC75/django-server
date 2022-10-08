from unittest.util import _MAX_LENGTH
from django.db import models

class Band(models.Model):
    name = models.fields.CharField(max_length=100)
    title = models.fields.CharField(max_length=100)

