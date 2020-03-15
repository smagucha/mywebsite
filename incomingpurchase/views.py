from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from .models import incoming_purchase
from .forms import incoming_purchaseform


@permission_required('can_view_incomingpurchase', login_url='/accounts/login/')
def incomingpurchaseview(request):
    if request.user.is_authenticated:
        objpurchase = incoming_purchase.objects.all()
        context = {
            'objpurchase': objpurchase
        }
        return render(request, 'incomingpurchase/incomingpurchaseview.html', context)
    else:
        return HttpResponseRedirect('login')


@permission_required('can_delete_incomingpurchase', login_url='/accounts/login')
def deleteincomingpurchase(request, id):
    if request.user.is_authenticated:
        del_id = incoming_purchase.objects.get(id=id)
        if request.method == 'POST':
            del_id.delete()
            return redirect('incomingpurchaseview')
        context = {
            'del_id': del_id
        }
        return render(request, 'incomingpurchase/deletepurchase.html', context)
    else:
        return HttpResponseRedirect('login')


@permission_required('Can_add_incoming_purchase', login_url='/accounts/login/')
def incoming_purchase_view(request):
    if request.user.is_authenticated:
        form = incoming_purchaseform(request.POST)
        if request.method == 'POST':
            form = incoming_purchaseform(request.POST)
            if form.is_valid():
                form.save()
                post = incoming_purchaseform()
                return HttpResponseRedirect('incomingpurchaseview')
        else:
            form = incoming_purchaseform()
        return render(request, 'incomingpurchase/incoming_purchase.html', {'form': form})
    else:
        return HttpResponseRedirect('login')
