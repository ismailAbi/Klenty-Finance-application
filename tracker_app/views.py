from django.shortcuts import render, redirect
from .models import Account, Expense, Budget
from .forms import AccountForm, ExpenseForm, BudgetForm


def index(request):
    accounts = Account.objects.all()
    expenses = Expense.objects.all()
    budget = Budget.objects.all()
    return render(request, 'tracker_app/index.html', {'accounts': accounts, 'expenses': expenses, 'budgets': budget})


def add_account(request):
    if request.method == 'POST':
        form = AccountForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = AccountForm()
    return render(request, 'tracker_app/add_account.html', {'form': form})


def add_expense(request):
    if request.method == 'POST':
        form = ExpenseForm(request.POST)
        if form.is_valid():
            accountName = form.cleaned_data['account']
            try:
                user = Account.objects.get(name=accountName)
                budget = Budget.objects.get(account=user)
            except Account.DoesNotExist:
                user = None
                budget = None
                return redirect('index')
            if (budget.amount - form.cleaned_data['amount']) >= 0:
                user.balance -= form.cleaned_data['amount']
                budget.amount -= form.cleaned_data['amount']
                form.save()
                user.save()
                budget.save()
            return redirect('index')
    else:
        form = ExpenseForm()
    return render(request, 'tracker_app/add_expense.html', {'form': form})


def add_budget(request):
    if request.method == 'POST':
        form = BudgetForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('index')
    else:
        form = BudgetForm()
    return render(request, 'tracker_app/add_budget.html', {'form': form})
