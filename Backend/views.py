from django.contrib.auth import authenticate,login
from django.contrib.auth.models import User
from django.core.files.storage import FileSystemStorage
from django.shortcuts import render,redirect
from django.utils.datastructures import MultiValueDictKeyError

from Backend.models import categorydb,productdb
from django.contrib import messages



# Create your views here.
def indexview(request):
    return render(request,"index.html")
def registercat(request):
    return render(request,"register.html")
def catsave(request):
    if request.method == "POST":
        cat = request.POST.get('category')
        des = request.POST.get('description')
        img = request.FILES['image']
        obj = categorydb(category=cat,description=des,image=img)
        obj.save()
        messages.success(request,"category saved sucessfully")
        return redirect(registercat)
def displaycat(request):
    data = categorydb.objects.all()
    return render(request,"tableview.html",{'data':data})
def editcat(request,c_id):
    category = categorydb.objects.get(id=c_id)
    return render(request,"edittable.html",{"category":category})
def deletecat(request,c_id):
    category = categorydb.objects.filter(id=c_id)
    category.delete()
    return redirect(displaycat)
def updatecat(request,c_id):
    if request.method == "POST":
        cat = request.POST.get('category')
        des = request.POST.get('description')
        try:
            img = request.FILES['image']
            fs =FileSystemStorage()
            file =fs.save(img.name,img)
        except MultiValueDictKeyError:
            file = categorydb.objects.get(id=c_id).image
        categorydb.objects.filter(id=c_id).update(category=cat, description=des, image=file)
        return redirect(displaycat)

def product(request):
    data = categorydb.objects.all()
    return render(request,"productadd.html",{'data':data})
def prodcutsave(request):
    if request.method == "POST":
        cat = request.POST.get('category')
        name = request.POST.get('name')
        des = request.POST.get('description')
        price = request.POST.get('price')
        image = request.FILES['image']
        obj = productdb(categorys=cat,name=name,description=des,price=price,image=image)
        obj.save()
        return redirect(product)
def displayproduct(request):
    data = productdb.objects.all()
    return render(request,"tableproduct.html",{'data':data})
def editproduct(request,p_id):
    product = productdb.objects.get(id=p_id)
    return render(request,"editproduct.html",{"product":product})
def updateproduct(request,p_id):
    if request.method == "POST":
        cat = request.POST.get('category')
        name = request.POST.get('name')
        des = request.POST.get('description')
        price = request.POST.get('price')
        try:
            image = request.FILES['image']
            fs = FileSystemStorage()
            file = fs.save(image.name, image)
        except MultiValueDictKeyError:
            file = productdb.objects.get(id=p_id).image
        productdb.objects.filter(id=p_id).update(categorys=cat, name=name, description=des, price=price, image=file)
        return redirect(displayproduct)

def deleteproduct(request,p_id):
    product = productdb.objects.filter(id=p_id)
    product.delete()
    return redirect(displayproduct)

def logicpage(request):
    return render(request,"login.html")
def adminlogin(request):
    if request.method == "POST":
        un = request.POST.get('uname')
        pwd = request.POST.get('password')

    if User.objects.filter(username__contains=un).exists():
        x = authenticate(username=un, password=pwd)
        if x is not None:
            return redirect(indexview)
        else:
            return redirect(logicpage)
    else:
        return redirect(adminlogin)