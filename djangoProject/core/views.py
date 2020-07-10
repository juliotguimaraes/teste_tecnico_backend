#coding=utf-8
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from .models import Compra
from .forms import CompraForm
from .serializers import CompraSerializer
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
    print(*compra_list, sep="\n")
    context['CompraSelecionado'] = CompraSelecionado
    context['compra_list'] = compra_list
    return render(request, template_name, context)

def listarCompras(request, pkCompra, pkdia, pkmes, pkano, pkdiaf, pkmesf, pkanof):
    template_name = 'compra/listaCompras.html'
    context = {}
    compra_list = Compra.objects.filter(product_id=pkCompra)


    #compras_selecionadas = compra_list.filter(product_id=pkCompra)
    dataini = str(pkano) + "-" + str(pkmes) + "-" + str(pkdia)
    datafim = str(pkanof) + "-" + str(pkmesf) + "-" + str(pkdiaf)

    lista_fim = compra_list.filter(date__range=[dataini,datafim])

    valorFinal = 0.0
    for compra in lista_fim:
        valorFinal += float(compra.total_value)

    print(compra_list[0])
    print("\n")
    print(valorFinal)

    return render(request, template_name, context)

def listarCompras2(request):
    template_name = 'compra/listaCompras.html'
    context = {}

    #print(request)

    return render(request, template_name, context)


    #compra = Compra.objects.get(product_id=pkCompra)



    #pisazonalizacaoSelecionada = PISazonalizacao()
    #proInfa = ProInfa.objects.get(pk=pkProInfa)
    #pisazonalizacao_list = PISazonalizacao.objects.filter(proInfa__id=proInfa.id)
    #if pk == '0':
    #    pisazonalizacaoSelecionada = pisazonalizacao_list[0]
    #else:
    #    pisazonalizacaoSelecionada = PISazonalizacao.objects.get(id=pk)
    #context['pisazonalizacao_list'] = pisazonalizacao_list
    #context['pisazonalizacaoSelecionada'] = pisazonalizacaoSelecionada
    #context['proInfaSelecionado'] = proInfa
    return render(request, template_name, context)
