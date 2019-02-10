from django.conf import settings
from django.db import models
from slugify import slugify


# Create your models here.


class Sport(models.Model):
	name = models.CharField(max_length=100, unique=True)
	image = models.ImageField(null=True)
	content = models.TextField(blank=True)

	active = models.BooleanField(default=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	@property
	def slug(self):
		return slugify(self.name)[:settings.DEFAULT_SLUG_LENGTH]
