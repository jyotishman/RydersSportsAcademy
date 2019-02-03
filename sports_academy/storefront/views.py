from rest_framework.views import View
from django.shortcuts import render

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
