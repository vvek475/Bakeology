from django.contrib import admin

# Register your models here.
from .models import posts
class posts_view(admin.ModelAdmin):
    list_display=['category','name','customer']
admin.site.register(posts,posts_view)