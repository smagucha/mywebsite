from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required
from .forms import stockform
from .models import stock


@permission_required('Can_view_newstock', login_url='/accounts/login/')
def stock_view(request):
    if request.user.is_authenticated:
        form = stockform(request.POST)
        if request.method == 'POST':
            form = stockform(request.POST)
            if form.is_valid():
                form.save()
                form = stockform()
                return HttpResponseRedirect('stockitem')
        else:
            form = stockform()
        return render(request, 'stock/stock.html', {'form': form})
    else:
        return HttpResponseRedirect('login')

@permission_required('Can_view_newstock', login_url='/accounts/login/')
def stockitem(request):
    if request.user.is_authenticated:
        object = stock.objects.all()
        context = {
            'object': object
        }
        return render(request, 'stock/stockitem.html', context)
    else:
        return redirect('login')

@permission_required('can_delete_newstock', login_url='/accounts/login/')
def deletestock(request, id):
    if request.user.is_authenticated:
        objectstock = stock.objects.get(id=id)
        if request.method == 'POST':
            objectstock.delete()
            return redirect('stockitem')
        context = {
            'objectstock': objectstock
        }
        return render(request, 'stock/deletestock.html', context)
    else:
        return redirect('login')


# Create your views here.
