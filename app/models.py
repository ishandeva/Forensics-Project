from django.db import models

class FileData(models.Model):
    account_number = models.BigIntegerField()
    date = models.DateField()
    details = models.CharField(max_length=500)
    withdrawal_amt = models.FloatField(null=True,blank=True)
    deposit_amt = models.FloatField(null=True,blank=True)
    balance = models.FloatField()

    def __str__(self):
        return f'{self.details}'
