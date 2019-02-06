from django.db import models

# Create your models here.


class Gallery(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField()
	description = models.TextField()

	priority = models.IntegerField()

	active = models.BooleanField(default=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		super(Gallery, self).save(*args, **kwargs)

