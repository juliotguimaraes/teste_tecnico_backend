#coding=utf-8
from django.conf.urls import include, re_path, url
from . import views


urlpatterns = [
    url(r'^core/$', views.compra, name='core'),
    url(r'^listar-compras/(?P<pkCompra>[0-9]+)/(?P<pkdia>[0-9]+)/(?P<pkmes>[0-9]+)/(?P<pkano>[0-9]+)/(?P<pkdiaf>[0-9]+)/(?P<pkmesf>[0-9]+)/(?P<pkanof>[0-9]+)/$', views.listarCompras, name='listar-compras'),
    url(r'^listar-compras2/$', views.listarCompras2, name='listar-compras2')
]
