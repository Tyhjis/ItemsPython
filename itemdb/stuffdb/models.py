from django.db import models
import datetime

# Create your models here.
class Item_type(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Role(models.Model):
	name = models.CharField(max_length=30)

	def __str__(self):
		return self.name

class Maker(models.Model):
	first_name = models.CharField(max_length=30)
	last_name = models.CharField(max_length=30)
	role = models.ForeignKey(Role, on_delete=models.CASCADE)

class Item(models.Model):
	item_type = models.ForeignKey(Item_type, on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	created_at = models.DateTimeField(auto_now_add=True)
	updated_at = models.DateTimeField(auto_now=True)
	makers = models.ManyToManyField(Maker)
	
	def __str__(self):
		return self.name