from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.HomeView.as_view(), name='home'),
    url(r'^centers/$', views.CenterView.as_view(), name='centers-list'),
    url(r'^center/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.CenterDetailView.as_view(), name='centers-detail'),
    url(r'^gallery/$', views.GalleryView.as_view(), name='galleries'),
    url(r'^sports/$', views.SportView.as_view(), name='sports'),
    url(r'^sport/(?P<pk>[0-9]+)/(?P<slug>[\w-]+)/$', views.SportDetailView.as_view(), name='sports-detail'),
    url(r'^center/(?P<pk>[0-9]+)/sports/$', views.SportCenterView.as_view(), name='center-sports'),
    url(r'^teams/$', views.TeamView.as_view(), name='teams'),
    url(r'^contact-us/$', views.ContactUsView.as_view(), name='contact_us'),
]