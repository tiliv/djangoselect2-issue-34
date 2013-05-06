from django.conf.urls import patterns, include, url

from .views import TestListView, TestCreateView, TestUpdateView

urlpatterns = patterns('',
    url(r'^$', TestListView.as_view(), name="list"),
    url(r'^create/$', TestCreateView.as_view(), name="create"),
    url(r'^(?P<pk>\d+)/$', TestUpdateView.as_view(), name="update"),
)
