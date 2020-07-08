#coding=utf-8
from django.shortcuts import render
from django.views import View
from django.shortcuts import get_object_or_404, redirect
from .models import Compra
from .forms import CompraForm
#from openpyxl import Workbook
from django.http import HttpResponse
#import xlwt

# Create your views here.

def compra(request):
    template_name = 'compra/compra.html'
    context = {}
    #proInfa_list = ProInfa.objects.all()
    #proInfaSelecionado = None
    #context['proInfa_list'] = proInfa_list
    #context['proInfaSelecionado'] = proInfaSelecionado
    return render(request, template_name, context)

def listarCompras(request, pkCompra, pk):
    template_name = 'compra/listaCompras.html'
    context = {}
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
