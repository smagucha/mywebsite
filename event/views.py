from django.shortcuts import render, redirect
from django.http import HttpResponseRedirect
from django.contrib.auth.decorators import permission_required
from .forms import myevent
from .models import events


@permission_required('can_view_event', login_url='/accounts/login/')
def event(request):
    if request.user.is_authenticated:
        eventobj = events.objects.all()
        context = {
            'eventobj': eventobj,
        }
        return render(request, 'event/event.html', context)
    else:
        return HttpResponseRedirect('login')


@permission_required('can_add_event', login_url='/accounts/login/')
def addevent(request):
    if request.user.is_authenticated:
        form = myevent(request.POST)
        if request.method == 'POST':
            form = myevent(request.POST)
            if form.is_valid():
                form.save()
                form = myevent()
            return HttpResponseRedirect('addevent')
        else:
            form = myevent()
        return render(request, 'event/addevent.html', {'form': form})
    else:
        return HttpResponseRedirect('login')


@permission_required('can_change_event', login_url='/accounts/login/')
def updateevent(request, id):
    if request.user.is_authenticated:
        updateformevnt = events.objects.get(id=id)
        updateformevnt = myevent(request.POST or None, instance=updateformevnt)
        if updateformevnt.is_valid():
            updateformevnt.save()
            updateformevnt = myevent()
            return redirect('event')
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
        delobj = events.objects.get(id=id)
        if request.method == 'POST':
            delobj.delete()
            return redirect('event')
        context = {
            'delobj': delobj
        }
        return render(request, 'event/deletevent.html', context)
    else:
        return redirect('login')
