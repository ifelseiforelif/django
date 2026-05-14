from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200, blank=False)
	created_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return f'{self.title}'
	
class Product(models.Model):
	title = models.CharField(max_length=30,blank=False)
	price = models.IntegerField(default=100)
	created_at = models.DateTimeField(auto_now=True)
	def __str__(self):
		return f'{self.title} {self.price}'