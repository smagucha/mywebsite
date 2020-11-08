from django.contrib import admin
from .models import Category, product

#admin.site.register(Category)
@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    list_filter = ['name','slug' ]

#admin.site.register(product)
@admin.register(product)
class  productAdmin(admin.ModelAdmin):
	list_display = ['name', 'description']
	list_filter = ['name', 'description']



