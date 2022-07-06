from django.shortcuts import render ,redirect
from datetime import datetime
from home.models import *
from django.contrib import messages


def index(request):
    
    cinema = cinema_house.objects.all()
    movi = movies.objects.all()
    mydata={
    'cinema':cinema,
    'movies':movi,
    }
    return render(request,'index.html',context=mydata)



def user_register(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        phone = request.POST.get('phone')
        password = request.POST.get('password')
        newuser = users(id = id,name= name,phone=phone,password=password,user_type=False)
        newuser.save()
    return render(request, 'admin_add_user.html')


def order_ticket(request, id):
    if request.method == "POST":
        id=request.POST.get('id')
        user = request.Cookie.get('userID')
        movie = request.POST.get('email')
        cinema = request.POST.get('address')
        price = request.POST.get('phone')
        x = ticket(id=id,user=user,movie=movie,cinema=cinema,price=price)
        x.save()
        return render(request, 'good.html')

    if request.method == "GET":
        a = movies.objects.get(id=id)
        return render(request, 'order.html', {'a': a})

def final(request):
        return render(request, 'good.html')

def good(request):
    return render(request, 'good.html')

#----------------------------------------------------------------------------------------------------------------------------
def admin_dashboard_view(request):
   
    cinemacount=cinema_house.objects.all().count()
    usercount=users.objects.all().count()
    ordercount=ticket.objects.all().count()
    moviescount=movies.objects.all().count()
    recent_orders = ticket.objects.all()

    
    orders=ticket.objects.all()
    ordered_products=[]
    ordered_bys=[]
    for order in orders:
        ordered_product=movies.objects.all().filter(id=order.medican)
        ordered_by=users.objects.all().filter(id = order.user)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)

    mydict={
    'cinemacount':cinemacount,
    'usercount':usercount,
    'ordercount':ordercount,
    'moviescount':moviescount,
    'recent_orders':recent_orders,
    }
    return render(request,'admin_dashboard.html',context=mydict)



def view_customer_view(request):
    user=users.objects.all()
    return render(request,'view_customer.html',{'customers':user})


def delete_customer_view(request,pk):
    user=users.objects.get(id=pk)
    user.delete()
    return redirect('view-customer')


def update_customer_view(request,pk):
    user=users.objects.get(id=pk)
    if request.method=='POST':
        id_from_frontend = request.POST.get('id')
        name_from_frontend = request.POST.get('name')
        phone_from_frontend = request.POST.get('phone')
        pass_from_frontend = request.POST.get('password')
        newuser = users(id = id_from_frontend,name= name_from_frontend,phone=phone_from_frontend,password=pass_from_frontend,user_type=False)
        newuser.save()
    return render(request,'admin_update_customer.html',{'id':pk})


def admin_movies_view(request):
    products=movies.objects.all()
    return render(request,'admin_products.html',{'products':products})



def add_new_movie(request):
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        med = movies(id= id,name= name)
        med.save()
    return render(request, 'admin_add_products.html')



def delete_product_view(request,pk):
    product=movies.objects.get(id=pk)
    product.delete()
    return redirect('admin-products')



def update_product_view(request,pk):
    product=movies.objects.get(id=pk)
    if request.method == "POST":
        id = request.POST.get('id')
        name = request.POST.get('name')
        med = movies(id= id,name= name)
        med.save()
        
    return render(request,'admin_update_product.html',{'pk':pk})



def admin_view_order_view(request):
    orders=ticket.objects.all()
    ordered_products=[]
    ordered_bys=[]
    for order in orders:
        ordered_product=movies.objects.all().filter(id=order.movie)
        ordered_by=users.objects.all().filter(id = order.user)
        ordered_products.append(ordered_product)
        ordered_bys.append(ordered_by)
    return render(request,'admin_view_booking.html',{'data':zip(ordered_products,ordered_bys,orders)})



def delete_order_view(request,pk):
    order=ticket.objects.get(id=pk)
    order.delete()
    return redirect('admin-view-booking')
