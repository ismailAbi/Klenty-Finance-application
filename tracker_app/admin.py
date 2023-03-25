from django.contrib import admin
from .models import Account, Expense,Budget

# Register your models here.


class AccountAdmin(admin.ModelAdmin):
    list_display = ('name', 'balance')

admin.site.register(Account, AccountAdmin)

class BudgetAdmin(admin.ModelAdmin):
    list_display = ('amount', 'account')
admin.site.register(Budget, BudgetAdmin)


class ExpenseAdmin(admin.ModelAdmin):
    list_display = ('name', 'amount', 'date', 'name')
admin.site.register(Expense, ExpenseAdmin)
