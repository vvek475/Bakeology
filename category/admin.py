from django.contrib import admin

from .models import category
class category_view(admin.ModelAdmin):
    list_display=['category','premium']
admin.site.register(category,category_view)
