from django.db import models

class Payment(models.Model):
    id = models.AutoField(primary_key=True)
    account = models.CharField(max_length=240)
    amount = models.FloatField(null=False)
    to_account = models.CharField(max_length=240, null=True)
    from_account = models.CharField(max_length=240, null=True)
    direction = models.CharField(max_length=8)

    def __str__(self):
        return self.account