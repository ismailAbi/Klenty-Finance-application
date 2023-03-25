from django.db import models


class Account(models.Model):
    name = models.CharField(max_length=50)
    balance = models.DecimalField(max_digits=10, decimal_places=2)

    class Meta:
        app_label = 'tracker_app'

    def __str__(self):
        return self.name


class Expense(models.Model):
    name = models.CharField(max_length=50)
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateField()
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        app_label = 'tracker_app'


class Budget(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    account = models.ForeignKey(Account, on_delete=models.CASCADE)

    class Meta:
        app_label = 'tracker_app'
