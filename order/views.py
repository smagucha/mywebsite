from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required
from .forms import orderusform
from .models import order


@permission_required('Can_add_neworderux', login_url='/accounts/login/')
def orderus_view(request):
    if request.user.is_authenticated:
        form = orderusform(request.POST)
        if request.method == 'POST':
            form = orderusform(request.POST)
            if form.is_valid():
                form.save()
                form = orderusform()
                return HttpResponseRedirect('vieworder')
        else:
            form = orderusform()
        return render(request, 'order/orderus.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


@login_required(login_url='accounts/login/')
def allorder(request):
    if request.user.is_authenticated:
        obj = order.objects.all()
        return render(request, 'order/allorders.html', {'obj': obj})
    else:
        return HttpResponseRedirect('login')


@permission_required('can_view_neworderux', login_url='/accounts/login')
def vieworder(request):
    if request.user.is_authenticated:
        objorder = order.objects.all()
        context = {
            'objorder': objorder
        }
        return render(request, 'order/vieworder.html', context)
    else:
        return HttpResponseRedirect('login')


@permission_required('can_delete_neworderux', login_url='/accounts/login')
def deleteorder(request, id):
    delobj = order.objects.get(id=id)
    if request.method == 'POST':
        delobj.delete()
        return redirect('vieworder')
    context = {
        'delobj': delobj
    }
    return render(request, 'order/deleteorder.html', context)
