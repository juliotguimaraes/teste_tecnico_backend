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
from django.http import HttpResponse
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.mixins import (
    CreateModelMixin, ListModelMixin, RetrieveModelMixin, UpdateModelMixin
)
from rest_framework.viewsets import GenericViewSet


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
    form = TotalVendidoForm(request.POST)
    for product in products: #filtra entre os ids requisitados
        compra_list = Compra.objects.filter(product_id=product)
        lista_fim = compra_list.filter(date__range=[date_ini,date_fim])
        for compra in lista_fim: #loop de todas as compras no date range
            dateini = compra.date
            valorFinal += float(compra.total_value)
            if compra.date > dateini: #valida para recomeçar a cada dia do laço
              dateini = compra.date
              context['ValorFinal'] = valorFinal
              endpoint = form.save(commit=False)
              if endpoint.is_valid():
                endpoint.date = compra.date
                endpoint.product_id = compra.product_id
                endpoint.total_value = valorFinal
                endpoint.save()
              lista_fim = []

    return render(request, template_name, context)
