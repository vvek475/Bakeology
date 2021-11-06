from django.contrib import admin

# Register your models here.
from .models import Orders
class Orders_view(admin.ModelAdmin):
    list_display=['name','size','cake_name']
admin.site.register(Orders,Orders_view)