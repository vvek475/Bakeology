from django.contrib import admin

# Register your models here.
from .models import cakespecs
class cakeSpecs_view(admin.ModelAdmin):
    list_display=['name','size','cake_name']
admin.site.register(cakespecs,cakeSpecs_view)