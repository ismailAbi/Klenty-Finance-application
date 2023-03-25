from django import forms
from .models import Expense, Account, Budget
import os

class ExpenseForm(forms.ModelForm):
    class Meta:
        model = Expense
        fields = ['name', 'amount', 'date', 'account']


class AccountForm(forms.ModelForm):
    class Meta:
        model = Account
        fields = ['name', 'balance']


class BudgetForm(forms.ModelForm):
    class Meta:
        model = Budget
        fields = ['amount', 'account']
