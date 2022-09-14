from django.contrib import admin

from .models import *

class CustomerAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'email', 'date_of_birth','date_created')
    search_fields = ('name', 'phone', 'email', 'date_of_birth')
    readonly_fields = ('date_created',)

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

class IncomeAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'date_updated', 'category', 'customer')
    search_fields = ('name', 'value', 'date_updated', 'category', 'customer')
    readonly_fields = ('date_created', 'date_updated')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'value', 'date_updated', 'category', 'customer')
    search_fields = ('name', 'value', 'date_updated', 'category', 'customer')
    readonly_fields = ('date_created', 'date_updated')

    filter_horizontal = ()
    list_filter = ()
    fieldsets = ()

admin.site.register(Income, IncomeAdmin)
admin.site.register(Expense, ExpenseAdmin)
admin.site.register(Message)
admin.site.register(Customer, CustomerAdmin)
