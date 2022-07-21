from django.db import models
from django.utils import timezone


# Create your models here.
class Category(models.Model):
    source = models.CharField(max_length=30)
    price = models.IntegerField()
    publish = models.DateTimeField(default=timezone.now)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self):
        return self.source
