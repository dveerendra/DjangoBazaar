from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from serializers import UserSerializer, GroupSerializer
import models

def index(request):
    return HttpResponse("Welcome to bazaar!")

def item(request, itemSlug):
	return HttpResponse("Item page with slug %s" % itemSlug)

def tag(request, tags):
	return HttpResponse("Tag page %s" % tags)

def search(request):
	return HttpResponse("Search page")

def profile(request):
	return HttpResponse("Profile page")



# API-views
class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """
    queryset = User.objects.all()
    serializer_class = UserSerializer


class GroupViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows groups to be viewed or edited.
    """
    queryset = Group.objects.all()
    serializer_class = GroupSerializer