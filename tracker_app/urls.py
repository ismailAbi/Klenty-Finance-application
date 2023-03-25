from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add_account/', views.add_account, name='add_account'),
    path('add_expense/', views.add_expense, name='add_expense'),
    path('add_budget/', views.add_budget, name='add_budget'),
]
