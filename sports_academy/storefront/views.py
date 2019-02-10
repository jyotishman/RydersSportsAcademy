import json
from django.shortcuts import render
from rest_framework.views import View
from sports_academy.gallery.models import Gallery
from sports_academy.center.models import Center
from sports_academy.sport.models import Sport
from django.shortcuts import get_object_or_404
from sports_academy.center.serializers import CenterSerializer
from sports_academy.sport.serializers import SportSerializer


# Create your views here.

global_context = {
		'centers': Center.objects.filter(active=True).only('id', 'academy_name').values('id', 'academy_name'),
		'sports': Sport.objects.filter(active=True).only('id', 'name').values('id', 'name'),
	}

class HomeView(View):
	template_name = "home.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
		}
		context.update(global_context)
		return render(request, self.template_name, context=context)


class GalleryView(View):
	template_name = "gallery.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
			'galleries': Gallery.objects.filter(active=True).only(
				'id', 'image', 'description'
			).values('id', 'image', 'description')
		}
		context.update(global_context)
		return render(request, self.template_name, context=context)


class CenterView(View):
	template_name = "centers.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
			'centres': json.loads(json.dumps(CenterSerializer(Center.objects.filter(active=True), many=True).data))
		}
		context.update(global_context)
		return render(request, self.template_name, context=context)


class CenterDetailView(View):
	template_name = "center-detail.html"

	def get(self, request, pk=None, *args, **kwargs):
		center = get_object_or_404(Center, pk=pk)
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
			'center': CenterSerializer(center).data
		}
		context.update(global_context)
		return render(request, self.template_name, context=context)


class SportView(View):
	template_name = "sports.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
			'sports': json.loads(json.dumps(SportSerializer(Sport.objects.filter(active=True), many=True).data))
		}
		context.update(global_context)
		return render(request, self.template_name, context=context)


class SportDetailView(View):
	template_name = "sport-detail.html"

	def get(self, request, pk=None, *args, **kwargs):
		sport = get_object_or_404(Sport, pk=pk)
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
			'sport': SportSerializer(sport).data
		}
		context.update(global_context)
		return render(request, self.template_name, context=context)


class SportCenterView(View):
	template_name = "sports-centers.html"

	def get(self, request, *args, **kwargs):
		sport = get_object_or_404(Sport, pk=pk)
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
		context.update(global_context)
		return render(request, self.template_name, context=context)


class TeamView(View):
	template_name = "teams.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
		context.update(global_context)
		return render(request, self.template_name, context=context)


class ContactUsView(View):
	template_name = "contact-us.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
		context.update(global_context)
		return render(request, self.template_name, context=context)
