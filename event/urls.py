from django.urls import path

from . import views 

urlpatterns = [
	path('event', views.event, name = "event"),
	path('addevent', views.addevent, name = "addevent"),
	path('updateevent/<int:id>/',views.updateevent, name = "updateevnt"),
	path('deleteevent/<int:id>/delete', views.deleteevent, name='deleteevent'),
]