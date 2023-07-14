from django.db import models

# Create your models here.
class DonateModel(models.Model):
    name=models.CharField(max_length=50)
    amount=models.IntegerField()
    payment_id=models.CharField(default=1,unique=True, max_length=100)
    paid=models.BooleanField(default=False)
    