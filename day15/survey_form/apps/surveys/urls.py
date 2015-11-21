from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^process_form$', views.process, name='process'),
    url(r'^result$', views.result, name='result')
)
