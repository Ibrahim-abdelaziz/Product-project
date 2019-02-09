from django.shortcuts import render ,redirect
from django.http import HttpResponse, HttpResponseRedirect
from .models import Product
from .forms import ProductForm, AddForm,MyForm
# Create your views here.

def all_product(request):
    data = Product.objects.all()

    return render(request,'allpro.html',{'data':data})

def one_product(request,name):
    datas=Product.objects.get(name=name)
    return render(request,'onepro.html',{'datas':datas})

def add_product(request):
    if request.method == 'GET':
        form = ProductForm()
    else:
        form = ProductForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            return redirect(all_product)
    return render(request,'add.html',{'addform':form})

def add(request):
    if request.method == 'GET':
        form = AddForm()
    else:
        form = AddForm(request.POST)
        if form.is_valid():
            proname = form.cleaned_data['name']
            proprice = form.cleaned_data['price']
            protype = form.cleaned_data['type']
            try:
                p = Product(name=proname,price=proprice,type=protype)
                p.save()
            except Exception as e:
                return HttpResponse(e)
            return redirect(all_product)
    return render(request, 'add.html', {'addform': form})

def new_form(request):
    if request.method == 'GET':
        form = MyForm()
    else:
        form = MyForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']
            send_email = (name,message,email,['ibrahim.abdelaziz1000@gmail.com'])
            return HttpResponse(' email sent')
    return render(request,'myform.html',{'myform': form})