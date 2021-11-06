from django.contrib import admin

# Register your models here.
from .models import review
class review_view(admin.ModelAdmin):
    list_display=['name','mobile','email','date']
admin.site.register(review,review_view)