from django.db import models

from cake.models import Cake

class cakespecs(models.Model):
    name=models.CharField(max_length=255)
    cake_name=models.CharField(max_length=100,default='Call')
    size=models.CharField(max_length=100)
    email=models.EmailField(max_length=100,default='demo@gmail.com')
    mob_number=models.CharField(max_length=15,default='+91 99999 99999')
    toppins=models.CharField(max_length=100,default='None')
    message=models.CharField(max_length=100,default='None')
    additionals=models.CharField(max_length=25)
    added_date=models.DateTimeField()
    

    def __str__(self):
        return str(self.name)