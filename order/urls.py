from django.urls import path
from . import views

urlpatterns = [
	path('allorder', views.allorder, name = "allorder"),
	path('orderus_view', views.orderus_view, name = "orderus_view"),
	path('vieworder', views.vieworder, name="vieworder"),
	path('deleteorder/<int:id>/delete', views.deleteorder, name="deleteorder")
]