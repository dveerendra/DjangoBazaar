from django.conf.urls import patterns, url
from django.conf.urls import url, patterns, include
from rest_framework import viewsets
from django.contrib import admin
from rest_framework import viewsets, routers
from django.contrib.auth.models import User, Group
from api import views
from api import views

class UserViewSet(viewsets.ModelViewSet):
    model = User

class GroupViewSet(viewsets.ModelViewSet):
    model = Group

router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'groups', GroupViewSet)

urlpatterns = patterns('',
    # ex: /
    #url (r'^users/$', views.UserViewSet.as_view()),
    url(r'^', include(router.urls)),
    url(r'^cms/(?P<cmsurl>\w+)', views.CMSView.as_view()),
    #url(r'^cms/', views.CMSView.as_view()),

)
