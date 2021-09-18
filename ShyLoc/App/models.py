from django.db import models

class data(models.Model):
    name = models.CharField(max_length = 40)
    description = models.TextField(max_length = 200)
    Subscriptions = models.TextField(max_length = 200)
    payment_due = models.DateField()
    payment_amount = models.TextField()   
    image = models.ImageField(blank=True, null=True)

    