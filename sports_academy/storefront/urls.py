from django.conf.urls import url

from . import views

sitemap_urlpatterns = [
    url(r'^sitemap\.xml$', views.SiteMapView.as_view(), name='sitemap'),
    url(r'^center-sitemap-(?P<page>\d+)\.xml$', views.CenterSiteMapView.as_view(), name='center-sitemap'),
    url(r'^sport-sitemap-(?P<page>\d+)\.xml$', views.SportSiteMapView.as_view(), name='sport-sitemap'),
]

urlpatterns = sitemap_urlpatterns + [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^centers/$', views.CenterView.as_view(), name='centers-view-list'),
    url(r'^center/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.CenterDetailView.as_view(), name='center-view-detail'),
    url(r'^gallery/$', views.GalleryView.as_view(), name='galleries'),
    url(r'^sports/$', views.SportView.as_view(), name='sports-view-list'),
    url(r'^sport/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.SportDetailView.as_view(), name='sport-view-detail'),
    url(r'^center/(?P<pk>[0-9]+)/sports/(?P<slug>[\w-]+)/$', views.SportCenterView.as_view(), name='center-sports'),
    url(r'^teams/$', views.TeamView.as_view(), name='teams'),
    url(r'^contact-us/$', views.ContactUsView.as_view(), name='contact-us'),
    url(r'^about-us/$', views.AboutUsView.as_view(), name='about-us')
]