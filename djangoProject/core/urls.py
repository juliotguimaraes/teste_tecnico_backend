#coding=utf-8
from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^core/$', views.compra, name='core'),
    url(r'^listar-compras/(?P<pkCompra>[0-9]+)/(?P<pk>[0-9]+)/$', views.listarCompras, name='listar-compras')
]
