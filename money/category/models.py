from django.db import models

# Create your models here.
class Category(models.Model):
	source = models.CharField(max_length = 30)
	price = models.IntegerField()
		