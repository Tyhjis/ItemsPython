from django.db import models

# Create your models here.
class Item_type(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Item(models.Model):
	item_type = models.ForeignKey(Item_type, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)

	def __str__(self):
		return self.name