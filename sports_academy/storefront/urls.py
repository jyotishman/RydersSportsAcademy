from django.conf.urls import url

from . import views

sitemap_urlpatterns = [
    url(r'^sitemap\.xml$', views.SiteMapView.as_view(), name='sitemap'),
    url(r'^home-page-sitemap\.xml$', views.HomeSiteMapView.as_view(), name='home-sitemap'),
    url(r'^center-sitemap-(?P<page>\d+)\.xml$', views.CenterSiteMapView.as_view(), name='center-sitemap'),
    url(r'^sport-sitemap-(?P<page>\d+)\.xml$', views.SportSiteMapView.as_view(), name='sport-sitemap'),
    url(r'^notification-sitemap-(?P<page>\d+)\.xml$', views.NotificationSiteMapView.as_view(),
        name='notification-sitemap'),
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
    url(r'^about-us/$', views.AboutUsView.as_view(), name='about-us'),
    url(r'^notifications/$', views.NotificationView.as_view(), name='notification-view-list'),
    url(r'^corporates/$', views.CorporateView.as_view(), name='corporate-view-list'),
    url(r'^visitors/$', views.VisitorsView.as_view(), name='visitors-view-list'),
    url(r'^reviews/$', views.ReviewsView.as_view(), name='reviews-view-list'),
    url(r'^media/$', views.MediaView.as_view(), name='media-view-list'),
    url(r'^notification/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.NotificationDetailView.as_view(),
        name='notification-view-detail'),
]
