from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required, login_required
from .forms import myform

from .models import mydatabase


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
            return redirect('contactdetails')
        context = {
            'form': my_form
        }
        return render(request, 'mysite/updatecontact.html', context)
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
