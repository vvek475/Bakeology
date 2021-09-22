from django.contrib import admin

# Register your models here.
from .models import Cake
class cake_view(admin.ModelAdmin):
    list_display=['category','name','ingredients']
admin.site.register(Cake,cake_view)