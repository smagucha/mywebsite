from django.contrib import admin
from .models import (
    mydatabase, MYPost, incoming_purchase,
    neworderux, newstock, salex, EVENTform, customerorder)


@admin.register(mydatabase)
class mydatabaseAdmin(admin.ModelAdmin):
    search_fields = ['firstname', 'surname', 'lastname', ]
    list_display = ['id','firstname', 'surname', 'lastname', 'email', ]
    list_filter = ['id','firstname', 'lastname', 'email', 'phonenumber']
    fieldsets = [
        ('Name', {'fields': ('firstname', 'lastname')}),
        ('contact', {'fields': ('phonenumber',)}),
        ('Location', {'fields': ('city',)})
    ]


admin.site.register(MYPost)
admin.site.register(incoming_purchase)
admin.site.register(customerorder)
admin.site.register(neworderux)
admin.site.register(newstock)
admin.site.register(salex)
admin.site.register(EVENTform)
# Register your models here.
