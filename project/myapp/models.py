from django.db import models

# Create your models here.

class Post(models.Model):
	title = models.CharField(max_length=200, blank=False)
	created_at = models.DateTimeField()
	def __str__(self):
		return f'{self.title}'
