from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.homepage, name='homepage'),
    url(r'^products$', views.index, name='index'),
    url(r'^products/(?P<product_id>\d+)$', views.product, name='product'),
    url(r'^products/update/(?P<product_id>\d+)$', views.update, name='update'),
    url(r'^products/delete/(?P<product_id>\d+)$', views.delete, name='delete'),
    url(r'^products/create$', views.create, name='create')
)
