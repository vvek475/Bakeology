from django.urls import path,include
from . import views

urlpatterns = [
    path('home',views.home,name='home'),
    path('placeorder',views.placeorder,name='placeorder'),
    path('review',views.review,name='review'),
    path('menu',views.menu,name='menu'),
    path('Check_order',views.Check_order,name='Check_order'),
    
]