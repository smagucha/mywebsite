from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse, HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required
from .forms import myform, PostForm, incoming_purchaseform, orderusform, stockform, salesform, myevent

from .models import (
    MYPost, mydatabase,
    incoming_purchase, neworderux, newstock, salex, EVENTform
)
from django.views import View


@login_required(login_url='/accounts/login/')
def index(request):
    if request.user.is_authenticated:
        return render(request, 'mysite/home.html')
    else:
        return HttpResponseRedirect('login')


@login_required(login_url='/accounts/login/')
def about(request):
    if request.user.is_authenticated:
        return render(request, 'mysite/about.html')
    else:
        return HttpResponseRedirect('login')


@login_required(login_url='/accounts/login/')
def thankyou(request):
    if request.user.is_authenticated:
        return render(request, 'mysite/thankyou.html')
    else:
        return HttpResponseRedirect('login')


@permission_required('Can_view_mydatabase', login_url='/accounts/login/')
def contactdetails(request):
    if request.user.is_authenticated:
        Mydatabase = mydatabase.objects.all()
        context = {
            'Mydatabase': Mydatabase
        }
        return render(request, 'mysite/contactdetails.html', context)
    else:
        return HttpResponseRedirect('login')


@permission_required('Can_add_mydatabase', login_url='/accounts/login/')
def contactform(request):
    if request.user.is_authenticated:
        form = myform(request.POST)
        if request.method == 'POST':
            form = myform(request.POST)
            if form.is_valid():
                form.save()
                form = myform()
            return HttpResponseRedirect('editcontact')
        else:
            form = myform()
        return render(request, 'mysite/contactform.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


@permission_required('Can_add_my_post', login_url='/accounts/login/')
def new_post(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST)
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                post = PostForm()
            return HttpResponseRedirect("staffpost")
        else:
            form = PostForm()
        return render(request, 'mysite/new_post.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


def my_view(request):
    if request.method == 'GET':
        # <view logic>
        return HttpResponse('<h3>result</h3>')


class MyView(View):
    def get(self, request):
        return HttpResponse('this is class based view')


class GreetingView(View):
    greeting = "Good Day"

    def get(self, request):
        return HttpResponse(self.greeting)


@permission_required('Can_add_my_post', login_url='/accounts/login/')
def editcontact(request):
    if request.user.is_authenticated:
        edit = mydatabase.objects.all()
        return render(request, 'mysite/editcontact.html', {'edit': edit})
    else:
        return HttpResponseRedirect('login')


@permission_required('Can_change_mydatabase', login_url='/accounts/login/')
def dynamic_lookup_view(request, id):
    if request.user.is_authenticated:
        obj = mydatabase.objects.get(id=id)
        my_form = myform(request.POST or None, instance=obj)
        if my_form.is_valid():
            my_form.save()
            my_form = myform()
        context = {
            'form': my_form
        }
        return render(request, 'mysite/updatecontact.html', context)
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
                return HttpResponseRedirect("incomingpurchaseview")
        else:
            form = incoming_purchaseform()
        return render(request, 'mysite/incoming_purchase.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


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
        return render(request, 'mysite/orderus.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


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
        return render(request, 'mysite/stock.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


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
        return render(request, 'mysite/sales.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


@login_required(login_url='accounts/login/')
def allorder(request):
    if request.user.is_authenticated:
        obj = neworderux.objects.all()
        return render(request, 'mysite/allorders.html', {'obj': obj})
    else:
        return HttpResponseRedirect('login')


@permission_required('can_view_event', login_url='/accounts/login/')
def event(request):
    if request.user.is_authenticated:
        eventobj = EVENTform.objects.all()
        context = {
            'eventobj': eventobj,
        }
        return render(request, 'mysite/event.html', context)
    else:
        return HttpResponseRedirect('login')


@permission_required('can_add_event', login_url='/accounts/login/')
def addevent(request):
    if request.user.is_authenticated:
        form = myevent(request.POST)
        if request.method == 'POST':
            form = myevent(request.POST)
            if eventform.is_valid():
                form.save()
                form = myevent()
            return HttpResponseRedirect('addevent')
        else:
            form = myevent()
        return render(request, 'mysite/addevent.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


# class contactdetaillist(ListView):
#	model = mydatabase
# queryset= mydatabase.objects.all()
#	template_name = 'mysite/contactdetails.html'
@login_required(login_url='/accounts/login/')
def stockorder(request):
    if request.user.is_authenticated:
        salesob = newstock.objects.all()
        obj2 = newstock.objects.all()
        context = {
            'salesob': salesob,
            'obj2': obj2,
        }
        return render(request, 'mysite/stockorder.html', {'salesob': salesob, 'obj2': obj2})
    else:
        return HttpResponseRedirect('login')


@permission_required('Can_delete_mydatabase', login_url='/accounts/login/')
def deletecontact(request, id):
    obj = get_object_or_404(mydatabase, id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('editcontact')
    context = {
        'object': obj
    }
    return render(request, 'mysite/deletecontact.html', context)


@permission_required('can_view_MYPost', login_url='/accounts/login/')
def staffpost(request):
    if request.user.is_authenticated:
        object = MYPost.objects.all()
        context = {
            'object': object
        }
        return render(request, 'mysite/staffpost.html', context)
    else:
        return redirect('login')


@permission_required('can_delete_MYPost', login_url='/accounts/login/')
def deletepost(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(MYPost, id=id)
        if request.method == 'POST':
            obj.delete()
            return redirect('staffpost')
        context = {
            'object': obj
        }
        return render(request, 'mysite/deletepost.html', context)
    else:
        return redirect('login')


@permission_required('Can_view_newstock', login_url='/accounts/login/')
def stockitem(request):
    if request.user.is_authenticated:
        object = newstock.objects.all()
        context = {
            'object': object
        }
        return render(request, 'mysite/stockitem.html', context)
    else:
        return redirect('login')


@permission_required('can_delete_newstock', login_url='/accounts/login/')
def deletestock(request, id):
    if request.user.is_authenticated:
        objectstock = newstock.objects.get(id=id)
        if request.method == 'POST':
            objectstock.delete()
            return redirect('stockitem')
        context = {
            'objectstock': objectstock
        }
        return render(request, 'mysite/deletestock.html', context)
    else:
        return redirect('login')


@permission_required('can_change_event', login_url='/accounts/login/')
def updateevent(request, id):
    if request.user.is_authenticated:
        updateformevnt = EVENTform.objects.get(id=id)
        updateformevnt = myevent(request.POST or None, instance=updateformevnt)
        if updateformevnt.is_valid():
            updateformevnt.save()
            updateformevnt = myevent()
            return  redirect('event')
        # redirect('event')
        context = {
            'updateformevnt': updateformevnt
        }
        return render(request, 'mysite/updateevent.html', context)
    else:
        return redirect('login')


@permission_required('can_delete_event', login_url='/accounts/login/')
def deleteevent(request, id):
    if request.user.is_authenticated:
        delobj = EVENTform.objects.get(id=id)
        if request.method == 'POST':
            delobj.delete()
            return redirect('event')
        context = {
            'delobj': delobj
        }
        return render(request, 'mysite/deletevent.html', context)
    else:
        return redirect('login')


@permission_required('can_delete_salex', login_url='/accounts/login/')
def deletesales(request, id):
    obj = salex.objects.get(id=id)
    if request.method == 'POST':
        obj.delete()
        return redirect('sales')
    context = {
        'obj': obj
    }
    return render(request, 'mysite/deletesales.html', context)


@permission_required('can_view_salex', login_url='/accounts/login/')
def sales_view(request):
    if request.user.is_authenticated:
        objsale = salex.objects.all()
        context = {
            'objsale': objsale
        }
        return render(request, 'mysite/salesview.html', context)
    else:
        return redirect('login')


@permission_required('can_change_salex', login_url='/accounts/login/')
def updatesales(request, id):
    if request.user.is_authenticated:
        updateoj = salex.objects.get(id=id)
        updateoj = salesform(request.POST or None, instance=updateoj)
        if updateoj.is_valid():
            updateoj.save()
            updateoj = salesform()
            return redirect('sales_view')
        context = {
            'updateoj': updateoj
        }
        return render(request, 'mysite/updatesales.html', context)
    else:
        return redirect('login')


@permission_required('can_view_incomingpurchase', login_url='/accounts/login/')
def incomingpurchaseview(request):
    if request.user.is_authenticated:
        objpurchase = incoming_purchase.objects.all()
        context = {
            'objpurchase': objpurchase
        }
        return render(request, 'mysite/incomingpurchaseview.html', context)
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
        return render(request, 'mysite/deletepurchase.html', context)
    else:
        return HttpResponseRedirect('login')


@permission_required('can_view_neworderux', login_url='/accounts/login')
def vieworder(request):
    if request.user.is_authenticated:
        objorder = neworderux.objects.all()
        context = {
            'objorder': objorder
        }
        return render(request, 'mysite/vieworder.html', context)
    else:
        return HttpResponseRedirect('login')


@permission_required('can_delete_neworderux', login_url='/accounts/login')
def deleteorder(request, id):
    delobj = neworderux.objects.get(id=id)
    if request.method == 'POST':
        delobj.delete()
        return redirect('vieworder')
    context = {
        'delobj': delobj
    }
    return render(request, 'mysite/deleteorder.html', context)
