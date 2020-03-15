from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required
from .forms import salesform
from .models import sale


@permission_required('Can_add_salex', login_url='/accounts/login/')
def sales(request):
    if request.user.is_authenticated:
        form = salesform(request.POST)
        if request.method == 'POST':
            form = salesform(request.POST)
            if form.is_valid():
                form.save()
                form = salesform()
                return redirect('sales_view')
            return HttpResponseRedirect('sales')
        else:
            form = salesform()
        return render(request, 'sales/sales.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


@permission_required('can_delete_salex', login_url='/accounts/login/')
def deletesales(request, id):
    obj = sale.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('sales')
    context = {
        'obj': obj
    }
    return render(request, 'sales/deletesales.html', context)


@permission_required('can_view_salex', login_url='/accounts/login/')
def sales_view(request):
    if request.user.is_authenticated:
        obj = sale.objects.all()
        # context ={'object': obj}
        return render(request, 'sales/salesview.html', {'obj': obj})
    else:
        return redirect('login')


@permission_required('can_change_salex', login_url='/accounts/login/')
def updatesales(request, id):
    if request.user.is_authenticated:
        updateoj = sale.objects.get(id=id)
        updateoj = salesform(request.POST or None, instance=updateoj)
        if updateoj.is_valid():
            updateoj.save()
            updateoj = salesform()
            return redirect('sales_view')
        context = {
            'updateoj': updateoj
        }
        return render(request, 'sales/updatesales.html', context)
    else:
        return redirect('login')
