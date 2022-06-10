from django.db import models
from store.models import ItemModel
from django.contrib.auth.models import User
# Create your models here.

class CartItem(models.Model):
    user = models.ForeignKey(User,on_delete = models.CASCADE)
    product = models.ForeignKey(ItemModel,on_delete = models.CASCADE)
    quantity = models.IntegerField()

