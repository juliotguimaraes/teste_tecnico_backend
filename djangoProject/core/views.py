#coding=utf-8
import json
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from django.views.decorators.csrf import csrf_exempt
from .models import Compra, TotalVendido
from .forms import CompraForm, TotalVendidoForm
from .serializers import CompraSerializer, TotalVendidoSerializer
from django.template.loader import get_template, render_to_string
#from openpyxl import Workbook
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet

#import xlwt

# Create your views here.

class CompraViewSet(GenericViewSet,  # generic view functionality
                     CreateModelMixin,  # handles POSTs
                     RetrieveModelMixin,  # handles GETs for 1 Company
                     UpdateModelMixin,  # handles PUTs and PATCHes
                     ListModelMixin):  # handles GETs for many Companies

      serializer_class = CompraSerializer
      queryset = Compra.objects.all()

def compra(request):
    template_name = 'compra/compra.html'
    context = {}
    compra_list = Compra.objects.all()
    CompraSelecionado = None

    context['CompraSelecionado'] = CompraSelecionado
    context['compra_list'] = compra_list
    return render(request, template_name, context)

#def listarCompras(request, pkCompra, pkdia, pkmes, pkano, pkdiaf, pkmesf, pkanof):
#    template_name = 'compra/listaCompras.html'
#    context = {}
#    compra_list = Compra.objects.filter(product_id=pkCompra)
#
#
#    #compras_selecionadas = compra_list.filter(product_id=pkCompra)
#    dataini = str(pkano) + "-" + str(pkmes) + "-" + str(pkdia)
#    datafim = str(pkanof) + "-" + str(pkmesf) + "-" + str(pkdiaf)
#
#    lista_fim = compra_list.filter(date__range=[dataini,datafim])
#
#    valorFinal = 0.0
#    for compra in lista_fim:
#        valorFinal += float(compra.total_value)
#
#    print(compra_list[0])
#    print("\n")
#    print(valorFinal)
#
#    return render(request, template_name, context)
#
###ListarCompras2 É a função response para POST, products é a lista de ids de produtos que será incluso na soma.
@csrf_exempt
def listarCompras(request):
    context = {}
    template_name = 'compra/listaCompras.html'

    json_data = json.loads(request.body) # request.raw_post_data w/ Django < 1.4
    try:
      products = json_data['products']
      date_ini = json_data['date_ini']
      date_fim = json_data['date_fim']
    except KeyError:
      HttpResponseServerError("Malformed data!")
    HttpResponse("Got json data")
    lista_fim = []
    valorFinal = 0.0
    for product in products:
        compra_list = Compra.objects.filter(product_id=product)
        lista_fim = compra_list.filter(date__range=[date_ini,date_fim])

        for compra in lista_fim:
            valorFinal += float(compra.total_value)
            print(valorFinal)
            lista_fim = []

    context['values'] = valorFinal
    #print(request)
    #compra = Compra.objects.get(product_id=pkCompra)
    return render(request, template_name, context)
