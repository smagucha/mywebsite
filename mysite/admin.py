from django.contrib import admin
from .models import mydatabase, customerorder


@admin.register(mydatabase)
class mydatabaseAdmin(admin.ModelAdmin):
    search_fields = ['firstname', 'surname', 'lastname', ]
    list_display = ['id', 'firstname', 'surname', 'lastname', 'email', ]
    list_filter = ['id', 'firstname', 'lastname', 'email', 'phonenumber']
    fieldsets = [
        ('Name', {'fields': ('firstname', 'lastname')}),
        ('contact', {'fields': ('phonenumber',)}),
        ('Location', {'fields': ('city',)})
    ]


admin.site.register(customerorder)
