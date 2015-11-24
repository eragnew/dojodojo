from django.conf.urls import patterns, url
import views

urlpatterns = patterns('',
    url(r'^$', views.index, name='index'),
    url(r'^products/add$', views.add, name='add'),
    url(r'^checkout$', views.checkout, name='checkout'),
    url(r'^products/delete/(?P<product_id>\d+)$', views.delete, name='delete'),
    url(r'^order$', views.order, name='order')
)
