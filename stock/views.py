
from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import permission_required, login_required
from .forms import  AddCatergory, AddProduct
from .models import  Category, product


@login_required
#@permission_required('Can_view_newstock', login_url='/accounts/login/')
def stock_view(request):
    if request.user.is_authenticated:
        form = AddProduct(request.POST)
        if request.method == 'POST':
            form = AddProduct(request.POST)
            if form.is_valid():
                form.save()
                form = AddProduct()
                return HttpResponseRedirect('stockitem')
        else:
            form = AddProduct()
        return render(request, 'stock/stock.html', {'form': form})
    else:
        return HttpResponseRedirect('login')

@login_required
#@permission_required('Can_view_newstock', login_url='/accounts/login/')
def stockitem(request):
    if request.user.is_authenticated:
        object1 = product.objects.all() 
        context = {
           'object1':object1,
            }
        return render(request, 'stock/stockitem.html', context)
    else:
        return redirect('login')

@login_required
#@permission_required('can_delete_newstock', login_url='/accounts/login/')
def deletestock(request, id):
    if request.user.is_authenticated:
        #question = get_object_or_404(Question, pk=question_id)
        objectstock = get_object_or_404(product, id=id)
        #objectstock = stock.objects.get(id=id)
        if request.method == 'POST':
            objectstock.delete()
            return redirect('stockitem')
        context = {
            'objectstock': objectstock
        }
        return render(request, 'stock/deletestock.html', context)
    else:
        return redirect('login')

@login_required
def updatestock(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(product, id = id)
        obj = AddProduct(request.POST or None, instance=obj)
        if obj.is_valid():
            obj.save()
            obj =AddProduct()
            return redirect('stockitem')
        context = {
            'obj': obj
        }
        return render(request, 'stock/updatestock.html', context)
    else:
        return HttpResponseRedirect('login')
#this has not be added to stock.html still configuring it out 
#the two methods addcatergory and addproduct

# Create your views here.

def addcatergory(request):
    if request.user.is_authenticated:
        form = AddCatergory(request.POST)
        if request.method == 'POST':
            form = AddCatergory(request.POST)
            if form.is_valid():
                form.save()
                form = AddCatergory()
                return HttpResponseRedirect('addproduct')    
        else:
            form = AddCatergory()
        return render(request, 'stock/addcatergory.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


def addproduct(request):
    if request.user.is_authenticated:
        form = AddProduct(request.POST)
        if request.method == 'POST':
            form = AddProduct(request.POST)
            if form.is_valid():
                form.save()
                form =AddProduct()
                return HttpResponseRedirect('stockitem')    
        else:
            form = AddProduct()
        return render(request, 'stock/addproduct.html', {'form': form})
    else:
        return HttpResponseRedirect('login')

