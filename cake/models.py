from django.db import models
from category.models import category

class Cake(models.Model):
    category=models.ForeignKey(category,default=1,on_delete=models.CASCADE)
    name=models.CharField(default='none',max_length=100)
    ingredients=models.TextField(default='none',max_length=550)
    toppings=models.CharField(default='none',max_length=255)
    making=models.TextField(default='none')
    cost=models.CharField(default='none',max_length=255)
    cake_pic=models.ImageField(upload_to='cake',blank=True,null=True)

    def __str__(self):
        return str(self.name)