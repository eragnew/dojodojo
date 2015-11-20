from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^ninja/(?P<color>\w+)/$', views.color, name='color'),
    url(r'^ninja/$', views.all, name='all'),
)
