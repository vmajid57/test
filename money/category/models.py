from django.db import models

# Create your models here.
class Category(models.Model):
	source = models.CharFields(max_length = 30)
	price = models.IntegerFields()
		