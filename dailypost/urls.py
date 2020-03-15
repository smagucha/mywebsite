from django.urls import path
from . import views 

urlpatterns = [
	path('new_post', views.new_post, name = "new_post"),  
	path('staffpost', views.staffpost, name = "staffpost"),
	path('deletepost/<int:id>/delete/', views.deletepost, name='deletepost'),
	
]