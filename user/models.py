from django.db import models

class User(models.Model):
    id = models.CharField(max_length=240, primary_key=True)
    balance = models.FloatField(default=0)
    currency = models.CharField(max_length=10)

    def __str__(self):
        return self.id