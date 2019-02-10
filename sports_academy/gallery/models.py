from django.conf import settings
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import F
from django.db.transaction import atomic
from slugify import slugify


# Create your models here.


class Gallery(models.Model):
	name = models.CharField(max_length=100)
	image = models.ImageField()
	description = models.TextField(blank=True)

	priority = models.IntegerField(null=True, blank=True)

	active = models.BooleanField(default=True)

	created = models.DateTimeField(auto_now_add=True)
	modified = models.DateTimeField(auto_now=True)

	def __str__(self):
		return "%s | Priority - %s"%(self.name, self.priority)

	def __init__(self, *args, **kwargs):
		super(Gallery, self).__init__(*args, **kwargs)
		self._prev_priority = self.priority

	def clean(self, *args, **kwargs):
		priority = self.priority
		max_priority = self.__class__.objects.count() if self.id else self.__class__.objects.count() + 1
		if priority and priority > max_priority:
			raise ValidationError("Priority should be greater than %s" % max_priority)
		if not self.priority:
			self.priority = max_priority
		super(Gallery, self).clean(*args, **kwargs)

	def save(self, *args, **kwargs):
		priority = self.priority
		prev_priority = self._prev_priority
		with atomic():
			if prev_priority and priority != prev_priority:
				if priority > prev_priority:
					self.__class__.objects.filter(
						priority__gt=prev_priority, priority__lte=priority
					).update(priority=F('priority') - 1)
				elif priority < prev_priority:
					self.__class__.objects.filter(
						priority__gte=priority, priority__lt=prev_priority
					).update(priority=F('priority') + 1)
			super(Gallery, self).save(*args, **kwargs)

	def delete(self, *args, **kwargs):
		priority = self.priority
		with atomic():
			self.__class__.objects.filter(priority__gt=priority).update(priority=F('priority') - 1)
			super(Gallery, self).delete(*args, **kwargs)

	@property
	def slug(self):
		return slugify(self.name)[:settings.DEFAULT_SLUG_LENGTH]
