from django.urls import path
from . import views

urlpatterns = [
	path('incoming_purchase_view', views.incoming_purchase_view, name = "incoming_purchase_view"),
	path('incomingpurchaseview',views.incomingpurchaseview, name="incomingpurchaseview"),
	path('deletepurchase/<int:id>/delete', views. deleteincomingpurchase, name="deleteincomingpurchase"),
	]
