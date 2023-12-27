from django.contrib import admin

# Register your models here.
from .models import Customer, CustomerContact

class CustomerContactInline(admin.StackedInline):
    model = CustomerContact
    extra = 0
    readonly_fields = ['created', 'updated']

class CustomerAdmin(admin.ModelAdmin):
    inlines = [CustomerContactInline]
    readonly_fields = ['created', 'updated']


admin.site.register(Customer, CustomerAdmin)

#admin.site.register(CustomerContact)