from django.db import models
from foods.models import Food



class UserPhone(models.Model):
    user_id = models.BigIntegerField(unique=True)
    phone = models.CharField(max_length=15)


class User(models.Model):
    user_id = models.BigIntegerField(unique=True)
    lang = models.CharField(max_length=10, null=True, blank=True)

class Basket(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    food = models.ForeignKey(Food, on_delete=models.CASCADE)
    count = models.PositiveIntegerField()


# Create your models here.
