from django.urls import path, include
from brighterMonday import views
from brighterMonday.job_api import JobViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register('jobs', JobViewSet, base_name='Job')

urlpatterns = [
    path('', views.index, name='home'),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include(router.urls))
]
