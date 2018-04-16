from django.conf.urls import url, include
from rest_framework import routers, urls

from disaster_app import views

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'groups', views.GroupViewSet)
router.register(r'neighborhoodunits', views.NeighborhoodUnitsSet)

urlpatterns = [
    url(r'^', include(router.urls)),
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]
