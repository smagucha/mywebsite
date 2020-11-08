from django.urls import path
from . import views

urlpatterns = [

	path('stockitem', views.stockitem, name = "stockitem"),
	path('stock_view', views.stock_view, name = "stock_view"),
	path('addcatergory', views.addcatergory, name = "addcatergory"),
	path('addproduct', views.addproduct, name = "addproduct"),
	path('deletestock/<int:id>/delete/', views.deletestock, name='deletestock'),
	path('updatestock/<int:id>/update', views.updatestock, name='updatestock'),
]