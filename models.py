from django.db import models

class User(models.Model):
    name = models.CharField(max_length=100)
    gender = models.BooleanField()  #True or false, True for women and false for men
    condition = models.CharField(max_length=100)
    email_phone_number = models.CharField(max_length=100)
    password = models.CharField(max_length=100)
    inventory = models.TextField()
    budget = models.DecimalField(max_digits=10, decimal_places=2)
    progress = models.TextField()
    points = models.IntegerField()
    credit_card = models.CharField(max_length=50, blank=False, null=False) #optional, depend of the user's account
    type_of_user = models.CharField(max_length=50)

    def __str__(self):
        return self.name
