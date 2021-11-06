from django.shortcuts import redirect, render
from django.http import HttpResponse
from cakespecs.models import Orders
from category.models import category
from cake.models import Cake
from posts.models import posts
from datetime import datetime
from review.models import review as Review
from django.contrib import messages

# Create your views here.
def home(request):
    Categories=category.objects.all().order_by('-id')
    post=posts.objects.all()
    cake=Cake.objects.all()[:6]
    reviews=Review.objects.all().order_by('-id')[:4]
    return render(request,'home.html',{
        'Categories':Categories,
        'posts':post,
        'cakes':cake,
        'reviews':reviews,
        })

def review(request):
    cake=Cake.objects.all()
    return render(request,'review.html',{'cakes':cake})

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
        order=Orders.objects.create(
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
            cost=cake.cost
            cost=int(cost[4:8])
            if size_=='Medium':
                cost=cost*2
            elif size_=='Large':
                cost=cost*3
                
        return render(request,'checkorder.html',{'order':order,'Cake':cakes,'cost':cost})


def orderPlaced(request):
    messages.error( request,'Thanks for the Ordering')
    return redirect('home')


def reviewPosted(request):
    if request.method=="POST":
        print(request.POST.get('cake_id'))
        Review.objects.create(
            cake_id=request.POST.get('cake_id'),
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            message=request.POST['message'],
            date=datetime.now(),
            pic=request.FILES.get('pic'),
        )
        messages.error( request,'Thanks for the Feedback')
        Categories=category.objects.all().order_by('-id')
        post=posts.objects.all()
        cake=Cake.objects.all()[:6]
        reviews=Review.objects.all().order_by('-id')[:4]
        return redirect('home')