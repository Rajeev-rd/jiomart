from django.shortcuts import render, redirect
from Backend.models import productdb, categorydb
from Frontend.models import ContactDb, RegistrationDb, Cartdb


# Create your views here.
def Home(request):
    pro = productdb.objects.all()
    data = categorydb.objects.all()
    return render(request, "Home.html", {'pro': pro, 'data': data})


def productpage(request, catname):
    data = categorydb.objects.all()
    pro = productdb.objects.filter(categorys=catname)
    return render(request, "product.html", {'pro': pro, 'data': data})


def aboutview(request):
    return render(request, "about.html")


def contactview(request):
    return render(request, "contact.html")


def singleproduct(request, proid):
    prod = productdb.objects.get(id=proid)
    return render(request, "singleproduct.html", {'prod': prod})


def contactsave(request):
    if request.method == 'POST':
        na = request.POST.get('name')
        em = request.POST.get('email')
        sub = request.POST.get('subject')
        mes = request.POST.get('message')
        obj = ContactDb(username=na, email=em, subject=sub, message=mes)
        obj.save()
        return redirect(contactview)


def loginsignup(request):
    return render(request, "loginsignup.html")


def saveuser(request):
    if request.method == 'POST':
        na = request.POST.get('username')
        em = request.POST.get('email')
        pas = request.POST.get('password')
        obj = RegistrationDb(username=na, email=em, password=pas)
        obj.save()
        return redirect(loginsignup)


def userlogin(request):
    if request.method == 'POST':
        un = request.POST.get('username')
        pwd = request.POST.get('password')
        if RegistrationDb.objects.filter(username=un, password=pwd).exists():
            request.session['username'] = un
            request.session['password'] = pwd
            return redirect(Home)
        else:
            return redirect(saveuser)
    else:
        return redirect(saveuser)


def userlogout(request):
    del request.session['username']
    del request.session['password']
    return redirect(loginsignup)


def cart(request):
    data = Cartdb.objects.filter(username=request.session['username'])
    return render(request, "cart.html", {'data': data})


def cartsave(request):
    if request.method == 'POST':
        x = request.POST.get('username')
        y = request.POST.get('productname')
        z = request.POST.get('price')
        T = request.POST.get('Total')
        obj = Cartdb(username=x, productname=y, price=z, Total=T)
        obj.save()
        return redirect(Home)


def cart_delete(request, p_id):
    x = Cartdb.objects.filter(id=p_id)
    x.delete()
    return redirect(cart)
