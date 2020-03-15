from django.urls import path
from . import views

urlpatterns = [
	path('stockitem', views.stockitem, name = "stockitem"),
	path('stock_view', views.stock_view, name = "stock_view"),
	path('deletestock/<int:id>/delete/', views.deletestock, name='deletestock'),
]