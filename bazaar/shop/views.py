from django.shortcuts import render
from django.http import HttpResponse

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