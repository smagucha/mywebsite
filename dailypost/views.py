from django.http import HttpResponseRedirect
from django.shortcuts import (redirect, render, get_object_or_404, )
from django.contrib.auth.decorators import permission_required
from .models import dailypost
from dailypost.forms import PostForm


@permission_required('can_view_MYPost', login_url='/accounts/login/')
def staffpost(request):
    if request.user.is_authenticated:
        object = dailypost.objects.all()
        context = {
            'object': object
        }
        return render(request, 'dailypost/staffpost.html', context)
    else:
        return redirect('login')


@permission_required('can_delete_MYPost', login_url='/accounts/login/')
def deletepost(request, id):
    if request.user.is_authenticated:
        obj = get_object_or_404(dailypost, id=id)
        if request.method == 'POST':
            obj.delete()
            return redirect('staffpost')
        context = {
            'object': obj
        }
        return render(request, 'dailypost/deletepost.html', context)
    else:
        return redirect('login')


@permission_required('Can_add_my_post', login_url='/accounts/login/')
def new_post(request):
    if request.user.is_authenticated:
        form = PostForm(request.POST)
        if request.method == 'POST':
            form = PostForm(request.POST)
            if form.is_valid():
                form.save()
                form = PostForm()
            return HttpResponseRedirect("staffpost")
        else:
            form = PostForm()
        return render(request, 'dailypost/new_post.html', {'form': form})
    else:
        return HttpResponseRedirect('login')
