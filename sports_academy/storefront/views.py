from django.shortcuts import render
from rest_framework.views import View
from sports_academy.center.models import Center
from sports_academy.sport.models import Sport
from django.shortcuts import get_object_or_404

# Create your views here.


class HomeView(View):
	template_name = "home.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
		return render(request, self.template_name, context=context)


class GalleryView(View):
	template_name = "gallery.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
		return render(request, self.template_name, context=context)


class CenterView(View):
	template_name = "centers.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
		return render(request, self.template_name, context=context)


class CenterDetailView(View):
	template_name = "center-detail.html"

	def get(self, request, pk=None, *args, **kwargs):
		center = get_object_or_404(Center, pk=pk)
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
		return render(request, self.template_name, context=context)


class SportView(View):
	template_name = "sports.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
		return render(request, self.template_name, context=context)


class SportDetailView(View):
	template_name = "sport-detail.html"

	def get(self, request, pk=None, *args, **kwargs):
		sport = get_object_or_404(Sport, pk=pk)
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
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
		return render(request, self.template_name, context=context)


class TeamView(View):
	template_name = "teams.html"

	def get(self, request, *args, **kwargs):
		context = {
			'meta_title': "Showtop10- The best 10 list of everything",
			'meta_description': "Top 10 list of everything and anything in one place. Get the best ten list everyday.",
			'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
		}
		return render(request, self.template_name, context=context)
