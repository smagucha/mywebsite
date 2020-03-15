from django.contrib import admin
from django.urls import path
from . import views 

urlpatterns = [
	path('deletecontact/<int:id>/delete/', views.deletecontact, name='deletecontact'),
	path('', views.index, name = "index	"),
	path('updatecontact/<int:id>/',views.dynamic_lookup_view, name = "dynamic_lookup_view"),
	path('about/', views.about, name = "about"),
	path('editcontact', views.editcontact, name = "editcontact"),
	path('thankyou', views.thankyou, name = "thankyou"),  
	path('contactform', views.contactform, name = "contactform"),
	path('contactdetails', views.contactdetails, name = "contactdetails"), 
]


