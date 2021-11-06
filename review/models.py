from datetime import datetime
from django.db import models
from django.db.models.fields.related import ForeignKey
from cake.models import Cake
# Create your models here.
class review(models.Model):
    cake=models.ForeignKey(Cake,on_delete=models.SET_NULL, null=True, blank=True, default=None)
    name=models.CharField(max_length=20,default='Customer')
    email=models.EmailField(max_length=50,default="customer@gmail.com")
    mobile=models.CharField(max_length=10,default='Cus_Num')
    message=models.TextField(max_length=500,default="Had the best cakes in the city")
    date=models.DateTimeField(default=datetime.now())
    pic=models.ImageField(upload_to='customers',blank=True,null=True)

    def __str__(self):
        return str(self.name)