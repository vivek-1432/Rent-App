from django.shortcuts import render, HttpResponse, redirect
from rentapp.models import prod
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout

# Create your views here.

def create(request):
    if request.method == 'GET':
        return render(request, 'create.html')
    else:
        name = request.POST['name']
        product = request.POST['product']
        price = request.POST['price']
        date = request.POST['date']
        till = request.POST['till']
        image = request.FILES['upload']

        
        m = prod.objects.create(name=name, product=product, price=price, date=date, till=till, image=image)
        m.save()
        return redirect('/')


def dashboard(request):
    m = prod.objects.all()
    context = {}
    context['data'] = m
    return render(request, 'dashboard.html', context)

def delete(request, rid):
    m = prod.objects.filter(id=rid)
    m.delete()
    return redirect('/dashboard')

def edit(request, rid):
    if request.method == 'GET':
        m = prod.objects.filter(id = rid)
        context = {}
        context['data'] = m
        return render(request, 'edit.html', context)
    
    else:
        xname = request.POST['xname']
        xproduct = request.POST['xproduct']
        xprice =request.POST['xprice']
        xdate =request.POST['xdate']
        xtill = request.POST['xtill']

        m = prod.objects.filter(id = rid)

        m.update(name = xname, product = xproduct, price = xprice, date = xdate, till = xtill)

        return redirect('/dashboard')

def home(request):
    return render(request, 'home.html')

def register(request):
    if request.method == 'GET':
        return render(request, 'register.html')
    else:
        uname=request.POST['uname']
        uemail=request.POST['uemail']
        upass=request.POST['upass']
        cpass=request.POST['cpass']

    if uname == "" or upass == "" or cpass == "":

        context = {}
        context['msg'] = 'fields cannot be empty'

        return render(request, 'register.html', context)
    
    elif upass != cpass:

        context = {}
        context['msg'] = 'password and confirm password should be same'

        return render(request, 'register.html', context)
    
    else:
        u = User.objects.create(username = uname, email = uemail)
        u.set_password(upass)
        u.save()
        return redirect('/register')


def user_login(request):
    if request.method == 'GET':
        return render(request, 'login.html')
    else:
        uname = request.POST['uname']
        upass = request.POST['upass']

        u = authenticate(username = uname, password = upass)

        if u is not None:
            login(request, u)
            return redirect('/')
        
        else:
            return HttpResponse("user not found")
        


def user_logout(request):
    logout(request)

    return redirect('/')

