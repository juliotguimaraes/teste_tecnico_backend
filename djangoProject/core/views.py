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

#import xlwt

# Create your views here.

def compra(request):
    template_name = 'compra/compra.html'
    context = {}
    compra_list = Compra.objects.all()
    CompraSelecionado = None
    print(*compra_list, sep="\n")
    context['CompraSelecionado'] = CompraSelecionado
    context['compra_list'] = compra_list
    return render(request, template_name, context)

def listarCompras(request):
    template_name = 'compra/listaCompras.html'
    context = {}
    serializer = CompraSerializer(date=request.date)

    print(serializer)
    #compra = Compra.objects.get(product_id=pkCompra)


    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
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
