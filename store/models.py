from re import T
from django.db import models

import string, random
from django.db.models.signals import pre_save
from django.dispatch import receiver
from django.utils.text import slugify

from project.util import unique_slug_generator
# Create your models here.

class ItemModel(models.Model):
    name = models.CharField(max_length=255,unique=True)
    slug = models.SlugField(default=None)
    price = models.IntegerField()
    description = models.CharField(max_length=2000)
    expiry = models.DateField()

    def __str__(self):
        return self.name

@receiver(pre_save, sender=ItemModel)
def pre_save_receiver(sender, instance, *args, **kwargs):
   if not instance.slug:
       instance.slug = unique_slug_generator(instance)