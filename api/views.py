from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User, Group
from rest_framework import viewsets
from api.serializers import UserSerializer, GroupSerializer
from rest_framework.views import APIView
from rest_framework import authentication, permissions
from rest_framework.response import Response
from shop import models
from django.http import Http404


# Create your views here.
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


# this view is used to handle all CMS interaction through collections
# and resources
class CMSView(APIView):
    permission_classes = (permissions.AllowAny,)    #CHANGE TO AUTHENTICATED LATER
    def get(self, request, cmsurl):
        #get the collection and resource names from url:
        splitpath = request.path.split('/');
        splitpath = splitpath[1:]

        #database query based on the words in array goes here###############
        queryset = models.MaterialCollections.objects.get()
        ####################################################################



        return Response(splitpath)
        #raise Http404




