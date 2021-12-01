from django.shortcuts import render, redirect, get_object_or_404, HttpResponseRedirect
from django.contrib.auth.decorators import login_required
from pedidos.models import STATUS_PEDIDO_CHOICES, MESAS_CHOICES, Pedido, Prato, Caixa
from pedidos.forms import PedidoForm, FormSetItemPedido, PagamentoForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.contrib import messages
from django.db.models import Sum

@login_required
def index(request):
  pedidos = Pedido.objects.all().order_by('-id')
  paginator = Paginator(pedidos, 6)
  page = request.GET.get('page')
  pedidos_por_pagina = paginator.get_page(page)
  
  data = {
    'pedidos': pedidos_por_pagina
  }
  return render(request,'home/index.html', data)

@login_required
def cardapio(request):
  pratos = Prato.objects.all().order_by('-id')
  paginator = Paginator(pratos, 6)
  page = request.GET.get('page')
  pratos_por_pagina = paginator.get_page(page)
  
  data = {
    'pratos': pratos_por_pagina
  }
  return render(request,'home/cardapio.html', data)


@login_required
def lista_pedidos(request):

  pratos = Prato.objects.all()
  data = {
    'pratos': pratos
  }
  return render(request,'home/lista_pedidos.html', data)


@login_required
def form_pedido(request):
    if request.method == 'POST':
        form = PedidoForm(request.POST)

        if form.is_valid():
            pedido = form.save(commit=False)
            pedido.usuario = request.user
            pedido.save()
            return redirect('atualizar_pedido', pk=pedido.id)
        else:
            return render(request, 'home/formPedido.html', {'form': form })
    else:
        form = PedidoForm()

    return render(request, 'home/formPedido.html', {'form': form })
  
  
@login_required
def atualizar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, id=pk)
    form = PedidoForm(request.POST or None, instance=pedido)
    form_set_items = FormSetItemPedido(request.POST or None, instance=pedido)
    data = {'form': form, 'pedido': pedido, 'form_items': form_set_items}
    
    if request.method == 'POST':
  
        if form.is_valid() and form_set_items.is_valid():
            form.save()
            form_set_items.save()
            return redirect('atualizar_pedido',  pk=pedido.id)
        else:
            return render(request, 'home/formPedido.html', data)

    return render(request, 'home/formPedido.html', data)


@login_required
def deletar_pedido(request, pk):
    pedido = get_object_or_404(Pedido, id=pk,)

    if request.method == "POST":
        pedido.delete()
        return HttpResponseRedirect("/")


@login_required
def mesas(request):

  mesas = MESAS_CHOICES
  data = {
    'mesas': mesas
  }
  return render(request,'home/mesas.html', data)


@login_required
def financeiro(request):
  
  caixas = Caixa.objects.all()
  total = Caixa.objects.all().aggregate(total_pagamentos=Sum('valor'))
  data = {
    'caixas': caixas,
    'total': total
  }
  return render(request,'home/financeiro.html', data)


@login_required
def pagamento(request, pk):
    pedido = get_object_or_404(Pedido, id=pk)
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        existe = Caixa.objects.filter(pedido=pedido).exists()
        valor_zerado = pedido.itens_pedido.count()
        if existe is False and valor_zerado>0:
          if form.is_valid():
              pagto = form.save(commit=False)
              pagto.valor = pedido.get_total_pedido
              pagto.pedido = pedido
              pagto.status=True
              pagto.save()
              return redirect('financeiro')
          else:
              return render(request, 'home/form_pagamento.html', {'form': form, 'pedido': pedido})
        else:
          if existe:
            messages.error(request, "Pedido ja em Caixa!")
          if valor_zerado == 0:
            messages.error(request, "Pedido sem valor!")
          return render(request, 'home/form_pagamento.html', {'form': form, 'pedido': pedido})
    else:
        form = PagamentoForm()

    return render(request, 'home/form_pagamento.html', {'form': form, 'pedido': pedido})
  
  
@login_required
def atualizar_status(request):
  status = STATUS_PEDIDO_CHOICES
  data = {
    'status': status
  }
  return render(request,'home/modal_fecha_pedido.html', data)