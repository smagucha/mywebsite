from django.urls import path
from django.contrib import admin

from . import views
urlpatterns = [
	
	path('sales_view',views.sales_view, name='sales_view'),
	path('updatesales/<int:id>/update',views.updatesales, name='updatesales'),
	path('deletesales/<int:id>/delete', views.deletesales, name='deletesales'),
	path('sales', views.sales, name = "sales"),

	]
