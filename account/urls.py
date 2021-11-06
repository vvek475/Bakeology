from django.urls import path,include
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('placeorder',views.placeorder,name='placeorder'),
    path('review',views.review,name='review'),
    path('menu',views.menu,name='menu'),
    path('Check_order',views.Check_order,name='Check_order'),
    path('order-placed',views.orderPlaced,name='orderPlaced'),
    path('review_posted',views.reviewPosted,name='review_posted'),
]