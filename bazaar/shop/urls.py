from django.conf.urls import patterns, url

from shop import views

urlpatterns = patterns('',
    # ex: /
    url(r'^$', views.index, name='index'),
    # ex: /item/<slug>/
    url(r'^item/(?P<itemSlug>\w+)/$', views.item, name='item'),
    # ex: /tag/<tag>/
    url(r'^shop/tag/(?P<tags>\w+)/$', views.tag, name='tag'),
    # ex: /search/<searchString>/
    url(r'^search/(?P<searchString>\w+)/$', views.search, name='search'),
    # ex: /profile/<id>/
    url(r'^profile/(?P<profileId>\w+)/$', views.profile, name='profile'),
)
