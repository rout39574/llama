from django.conf.urls import patterns, url

from tut import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index')
)
