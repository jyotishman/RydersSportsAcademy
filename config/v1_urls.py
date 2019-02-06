from django.conf.urls import include, url
from rest_framework import routers

from sports_academy.center import views as center_views
from sports_academy.gallery import views as gallery_views
from sports_academy.sport import views as sport_views
from sports_academy.team import views as team_views

router = routers.DefaultRouter()
router.register(r'center', center_views.CenterViewSet, base_name='centers')
router.register(r'gallery', gallery_views.GalleryViewSet, base_name='galleries')
router.register(r'sport', sport_views.SportViewSet, base_name='sports')
router.register(r'team', team_views.TeamViewSet, base_name='teams')

urlpatterns = [
	url(r'', include(router.urls)),
]
