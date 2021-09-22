from django.db.models.deletion import CASCADE
from django.db.models.fields import CharField
from django.db.models.fields.files import ImageField
from django.db.models.fields.related import ForeignKey
from category.models import category
from django.db import models
from category.models import category
from cake.models import Cake
from django.utils.timezone import timezone


class posts(models.Model):
    category=models.ForeignKey(category,on_delete=CASCADE)
    customer=models.CharField(max_length=255)
    name=models.CharField(max_length=255)
    review=models.TextField(max_length=550,default='Fine')
    date_time=models.DateTimeField()
    customer_pic=models.ImageField(upload_to='customers',blank=True,null=True)
    cake_pic=models.ImageField(upload_to='cake',blank=True,null=True)
    
    def __str__(self):
        return str(self.customer)

    