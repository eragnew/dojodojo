from django.conf.urls import patterns, url
# from apps.quiz import views
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
)
