from django.conf.urls import patterns, include, url

urlpatterns = patterns('',
    url(r'^', include('ds2_issue34.testapp.urls')),
    url(r'^', include('django_select2.urls')),
)
