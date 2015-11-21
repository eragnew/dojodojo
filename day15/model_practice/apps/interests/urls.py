from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^interests/(?P<user_id>\d+)/$', views.one, name='one'),
    url(r'^interests/$', views.all, name='all'),
)
