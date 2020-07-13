#coding=utf-8
from django.conf.urls import include, re_path, url
from . import views

urlpatterns = [
    url(r'^core/$', views.compra, name='core'),
    url(r'^listar-compras/$', views.listarCompras, name='listar-compras')
]
