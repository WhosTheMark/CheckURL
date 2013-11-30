from django.conf.urls import patterns, url

from checkUrl import views

urlpatterns = patterns('',
    url(r'^$', views.home, name='home')
)