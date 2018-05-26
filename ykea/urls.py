from django.conf.urls import url

from . import views

urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^items/$', views.items, name='items'),
    url(r'^items/(?P<category>.*)/$', views.items, name='items'),
    url(r'^item/(?P<id>.*)/$', views.details, name='details'),
    url(r'^shoppingcart/$', views.shoppingcart, name='shoppingcart'),
    url(r'^buy/$', views.buy, name='buy'),
    url(r'^buy/process/$', views.process, name='process'),
    url(r'^buy/delete/$', views.delete, name='delete'),
    url(r'^buy/checkout/$', views.checkout, name='checkout')
]