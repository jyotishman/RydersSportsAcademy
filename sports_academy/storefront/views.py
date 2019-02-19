from math import ceil
from urllib.parse import urljoin

from django.conf import settings
from django.shortcuts import get_object_or_404
from django.shortcuts import render
from django.urls import reverse
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.views import View
from rest_framework.viewsets import ViewSet

from sports_academy.brands.models import Brands
from sports_academy.center.models import Center
from sports_academy.center.serializers import CenterSerializer, CenterDetailSerializer
from sports_academy.company.models import Company
from sports_academy.gallery.models import Gallery
from sports_academy.sport.models import Sport
from sports_academy.sport.serializers import SportSerializer, SportDetailSerializer
from sports_academy.team.models import Team
from sports_academy.team.serializers import TeamDetailSerializer
from sports_academy.utils.helpers import CreateXMLContext, convert_to_dict
from . import serializers


# Create your views here.


def global_context():
    return {
        'centers': Center.objects.filter(active=True).only(
            'id', 'academy_name', 'slug'
        ).values('id', 'academy_name', 'slug'),
        'sports': Sport.objects.filter(active=True).only(
            'id', 'name', 'image', 'slug'
        ).values('id', 'name', 'image', 'slug'),
        'company': Company.objects.values()[0] if Company.objects.exists() else {}
    }


class HomeView(View):
    template_name = "home.html"

    def get(self, request, *args, **kwargs):
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
            'brands': Brands.objects.filter(active=True).only('id', 'name', 'image').values('id', 'name', 'image'),
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class GalleryView(View):
    template_name = "gallery.html"

    def get(self, request, *args, **kwargs):
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
            'galleries': Gallery.objects.filter(active=True).only(
                'id', 'image', 'description'
            ).values('id', 'image', 'description')
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class CenterView(View):
    template_name = "centers.html"

    def get(self, request, *args, **kwargs):
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
            'centres': convert_to_dict(CenterSerializer(Center.objects.filter(active=True), many=True).data)
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class CenterDetailView(View):
    template_name = "center-detail.html"

    def get(self, request, pk=None, *args, **kwargs):
        center = get_object_or_404(Center, pk=pk)
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
            'center': convert_to_dict(CenterDetailSerializer(center).data)
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class SportView(View):
    template_name = "sports.html"

    def get(self, request, *args, **kwargs):
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
            'sports': convert_to_dict(SportSerializer(Sport.objects.filter(active=True), many=True).data)
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class SportDetailView(View):
    template_name = "sport-detail.html"

    def get(self, request, pk=None, *args, **kwargs):
        sport = get_object_or_404(Sport, pk=pk)
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
            'sport': convert_to_dict(SportDetailSerializer(sport).data)
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class SportCenterView(View):
    template_name = "sports-centers.html"

    def get(self, request, pk=None, *args, **kwargs):
        center = get_object_or_404(Center, pk=pk)
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
            'center': convert_to_dict(CenterDetailSerializer(center).data)
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class TeamView(View):
    template_name = "teams.html"

    def get(self, request, *args, **kwargs):
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png",
            'teams': convert_to_dict(TeamDetailSerializer(Team.objects.filter(active=True), many=True).data)
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class ContactUsView(View):
    template_name = "contact-us.html"

    def get(self, request, *args, **kwargs):
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class ContactUsViewSet(ViewSet):
    permission_classes = (AllowAny,)
    http_method_names = ["post"]

    def create(self, request, *args, **kwargs):
        serializer = serializers.ContactUsSerializer(data=request.data)
        if serializer.is_valid():
            mail_response = serializer.create(serializer.validated_data)
            return Response({'send': mail_response})
        else:
            return Response(serializer.errors, status=400)


class AboutUsView(View):
    template_name = "about-us.html"

    def get(self, request, *args, **kwargs):
        context = {
            'meta_title': "RydersSportsAcademy",
            'meta_description': "Ryders Sport's Academy",
            'image': "https://d14nytznni7htl.cloudfront.net/standalone/17663/og_image_1542134794_7567792.png"
        }
        context.update(global_context())
        return render(request, self.template_name, context=context)


class SiteMapView(View):

    def get(self, request, *args, **kwargs):
        xml_content = CreateXMLContext(settings.WEB_BASE_URL, settings.MEDIA_URL)

        static_url_n_changefreqs = [
            (reverse('home'), 'monthly'),
            (reverse('contact-us'), 'monthly'),
            (reverse('about-us'), 'monthly'),
        ]

        for (url, changefreq) in static_url_n_changefreqs:
            xml_content.create_xml_url_context(url, changefreq=changefreq)

        gallery_lastmod = Gallery.objects.order_by('-modified').first().modified
        gallery_images = Gallery.objects.values_list('image', flat=True)

        xml_content.create_xml_url_context(reverse('galleries'), lastmod=gallery_lastmod, images=gallery_images)

        team_lastmod = Team.objects.order_by('-modified').first().modified

        xml_content.create_xml_url_context(reverse('teams'), lastmod=team_lastmod)

        if Center.objects.exists():
            center_list = [reverse('center-sitemap', kwargs={'page': index}) for index in range(1, ceil(
                Center.objects.count() / settings.XML_PAGINATION_CONSTANTS.get('center', 50)
            ) + 1)]
            center_lastmod = Sport.objects.order_by('-modified').first().modified
            for center_list in center_list:
                xml_content.create_xml_sitemap_context(center_list, lastmod=center_lastmod)

        if Sport.objects.exists():
            sport_list = [reverse('sport-sitemap', kwargs={'page': index}) for index in range(1, ceil(
                Sport.objects.count() / settings.XML_PAGINATION_CONSTANTS.get('sport', 50)
            ) + 1)]
            sport_lastmod = Sport.objects.order_by('-modified').first().modified
            for sport_url in sport_list:
                xml_content.create_xml_sitemap_context(sport_url, lastmod=sport_lastmod)

        return render(request, 'sitemap.xml', xml_content.generate_xml_context, content_type="text/xml")


class CenterSiteMapView(View):
    def get(self, request, page, *args, **kwargs):
        xml_content = CreateXMLContext(settings.WEB_BASE_URL, settings.MEDIA_URL)
        start = (int(page) - 1) * int(settings.XML_PAGINATION_CONSTANTS.get('center', 50))
        end = int(page) * settings.XML_PAGINATION_CONSTANTS.get('center', 50)
        for center in Center.objects.all()[start:end]:
            xml_content.create_xml_url_context(
                urljoin(settings.WEB_BASE_URL, f"/center/{center.id}/{center.slug}"),
                lastmod=str(center.modified),
                images=[center.image] if center.image else []
            )
        return render(request, 'sitemap.xml', xml_content.generate_xml_context, content_type="text/xml")


class SportSiteMapView(View):
    def get(self, request, page, *args, **kwargs):
        xml_content = CreateXMLContext(settings.WEB_BASE_URL, settings.MEDIA_URL)
        start = (int(page) - 1) * int(settings.XML_PAGINATION_CONSTANTS.get('sport', 50))
        end = int(page) * settings.XML_PAGINATION_CONSTANTS.get('sport', 50)
        for sport in Sport.objects.all()[start:end]:
            xml_content.create_xml_url_context(
                urljoin(settings.WEB_BASE_URL, f"/sport/{sport.id}/{sport.slug}"),
                lastmod=str(sport.modified),
                images=[sport.image] if sport.image else []
            )
        return render(request, 'sitemap.xml', xml_content.generate_xml_context, content_type="text/xml")
