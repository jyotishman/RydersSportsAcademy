from django.conf import settings
from django.db import models
from slugify import slugify


# Create your models here.


class Team(models.Model):
	name = models.CharField(max_length=200)
	image = models.ImageField()
	designation = models.CharField(max_length=100)

	about = models.TextField(blank=True)

	active = models.BooleanField(default=True)

	sports = models.ManyToManyField('sport.Sport')
	centers = models.ManyToManyField('center.Center')

	twitter_url = models.URLField(max_length=200, blank=True)
	facebook_url = models.URLField(max_length=200, blank=True)
	instagram_url = models.URLField(max_length=200, blank=True)
	google_plus_url = models.URLField(max_length=200, blank=True)
	linkedin_url = models.URLField(max_length=200, blank=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return self.name

	@property
	def slug(self):
		return slugify(self.name)[:settings.DEFAULT_SLUG_LENGTH]
