from django.shortcuts import render
from django.http import HttpResponse
from cakespecs.models import cakespecs
from category.models import category
from cake.models import Cake
from posts.models import posts
from datetime import datetime
# Create your views here.
def home(request):
    Categories=category.objects.all().order_by('-id')
    post=posts.objects.all()
    cake=Cake.objects.all()
    return render(request,'home.html',{
        'Categories':Categories,
        'posts':post,
        'cakes':cake
        })

def review(request):
    Categories=category.objects.all().order_by('-id')
    return render(request,'review.html',{'Categories':Categories})

def placeorder(request):
    cake=Cake.objects.all()
    Categories=category.objects.all().order_by('-id')
    return render(request,'placeOrder.html',{'Categories':Categories,'cakes':cake})

def menu(request):
    cake=Cake.objects.all()
    Categories=category.objects.all().order_by('-id')
    return render(request,'menu.html',{'cakes':cake,'Categories':Categories})

def Check_order(request):
    if request.method=='POST':
        order=cakespecs.objects.create(
            name= request.POST['name'],
            cake_name=request.POST['cake'],
            size=request.POST['size'],
            email=request.POST['Email'],
            mob_number=request.POST['mobile'],
            toppins=request.POST['toppins'],
            message=request.POST['message'],
            additionals=request.POST['additionals'],
            added_date=datetime.now()
        )

        cakes=Cake.objects.filter(name=order.cake_name)
        for cake in cakes:
            size_=order.size
            print(size_)
            cost=cake.cost
            cost=int(cost[4:8])
            if size_=='Medium':
                cost=cost*2
            elif size_=='Large':
                cost=cost*3
        print(cost)
        return render(request,'checkorder.html',{'order':order,'Cake':cakes,'cost':cost})

    else:
        return HttpResponse(str('wrongone'))