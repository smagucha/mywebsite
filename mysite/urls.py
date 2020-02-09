from django.contrib import admin
from django.urls import path
from . import views 
from .views import MyView, GreetingView
urlpatterns = [
	#path('contactdetails', contactdetaillist.as_view(), name=' contactdetails'),
	path('deletecontact/<int:id>/delete/', views.deletecontact, name='deletecontact'),
	path('', views.index, name = "index	"),
	path('allorder', views.allorder, name = "allorder"),
	path('stockorder', views.stockorder, name = "stockorder"),
	path('updatecontact/<int:id>/',views.dynamic_lookup_view, name = "dynamic_lookup_view"),
	path('about/', views.about, name = "about"),
	path('event', views.event, name = "event"),
	path('stockitem', views.stockitem, name = "stockitem"),
	path('addevent', views.addevent, name = "addevent"),
	path('stock_view', views.stock_view, name = "stock_view"),
	path('sales', views.sales, name = "sales"),
	path('editcontact', views.editcontact, name = "editcontact"),
	path('orderus_view', views.orderus_view, name = "orderus_view"),
	path('incoming_purchase_view', views.incoming_purchase_view, name = "incoming_purchase_view"),
	path('MyView/', MyView.as_view(), name="MyView"),
	path('GreetingView/', GreetingView.as_view(), name="GreetingView"),
	path('my_view', views.my_view, name = "my_view"),
	path('thankyou', views.thankyou, name = "thankyou"),
	path('new_post', views.new_post, name = "new_post"),  
	path('contactform', views.contactform, name = "contactform"),
	path('index', views.index, name = "index"),
	path('staffpost', views.staffpost, name = "staffpost"),
	path('deletepost/<int:id>/delete/', views.deletepost, name='deletepost'),
	path('deletestock/<int:id>/delete/', views.deletestock, name='deletetock'),
	path('contactdetails', views.contactdetails, name = "contactdetails"), 
	path('updateevent/<int:id>/',views.updateevent, name = "updateevnt"),
	path('deleteevent/<int:id>/delete', views.deleteevent, name='deleteevent'),
	path('deletesales/<int:id>/delete', views.deletesales, name='deletesales'),
	path('sales_view',views.sales_view, name='sales_view'),
	path('updatesales/<int:id>/update',views.updatesales, name='updatesales'),
	path('incomingpurchaseview',views.incomingpurchaseview, name="incomingpurchaseview"),
	path('deletepurchase/<int:id>/delete', views. deleteincomingpurchase, name=" deleteincomingpurchase"),
	path('vieworder', views.vieworder, name="vieworder"),
	path('deleteorder/<int:id>/delete', views.deleteorder, name="deleteorder")
]


