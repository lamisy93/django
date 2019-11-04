from rest_framework import routers, serializers, viewsets
from django.urls import path
from django.conf.urls import url, include

from . import views

router = routers.DefaultRouter()

router.register(r'members', views.MemberViewSet)

app_name = 'member'
urlpatterns = [
    url(r'^', include(router.urls)),
    # /members/add
    path('add/', views.addMember, name='add_member'),
]
