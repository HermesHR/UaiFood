from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from pedidos.models import Pedido, Prato

@login_required
def index(request):

  pedidos = Pedido.objects.all()
  data = {
    'pedidos': pedidos
  }
  return render(request,'home/index.html', data)


@login_required
def cardapio(request):

  pratos = Prato.objects.all()
  data = {
    'pratos': pratos
  }
  return render(request,'home/cardapio.html', data)


@login_required
def enviapedido(request):

  pratos = Prato.objects.all()
  data = {
    'pratos': pratos
  }
  return render(request,'home/enviapedido.html', data)


@login_required
def mesas(request):

  pedidos = Pedido.objects.all()
  data = {
    'pedidos': pedidos
  }
  return render(request,'home/mesas.html', data)