from autoslug import AutoSlugField
from django.db import models


# Create your models here.


class Company(models.Model):
	name = models.CharField(max_length=100, unique=True)
	twitter_url = models.URLField(max_length=200, blank=True)
	facebook_url = models.URLField(max_length=200, blank=True)
	instagram_url = models.URLField(max_length=200, blank=True)
	google_plus_url = models.URLField(max_length=200, blank=True)
	linkedin_url = models.URLField(max_length=200, blank=True)
	address = models.TextField(blank=True)
	city = models.CharField(max_length=100)
	state = models.CharField(max_length=100)
	country = models.CharField(max_length=100)
	zipcode = models.CharField(max_length=10)
	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name
