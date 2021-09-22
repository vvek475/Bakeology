from django.db import models
from django.db.models.fields import CharField

class category(models.Model):
    category=models.CharField(max_length=100)
    premium=models.BooleanField(default=False)


    def __str__(self):
        return str(self.category)