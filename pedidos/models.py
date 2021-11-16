from django.db import models
from django.contrib.auth.models import User
from django.db.models.functions import Coalesce
from django.db.models import Sum, Value
from decimal import Decimal

STATUS_CHOICES = (
      (0, "Disponível"),
      (1, "Indisponível")
    )

STATUS_PEDIDO_CHOICES = (
      (1, "EM ANDAMENTO"),
      (2, "PAGO"),
      (3, "PRONTO")

    )

MESAS_CHOICES = (
    (1, "MESA 01"),
    (2, "MESA 02"),
    (3, "MESA 03"),
    (4, "MESA 04"),
    (5, "MESA 05")
  )

class Categoria(models.Model):
  nome = models.CharField(max_length=100)
  descricao = models.CharField(max_length=100)

  def __str__(self):
    return self.nome

class Prato(models.Model):
  nome = models.CharField(max_length=100)
  categoria = models.ForeignKey(Categoria, on_delete=models.CASCADE)
  descricao = models.CharField(max_length=100)
  status = models.BooleanField(choices=STATUS_CHOICES)
  valor = models.DecimalField(max_digits=5, decimal_places=2)
  criado = models.DateTimeField(auto_now_add=True)
  atualizado = models.DateTimeField(auto_now=True)

  def __str__(self):
    return self.nome


class Pedido(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  data = models.DateTimeField(auto_now_add=True)
  mesa = models.IntegerField(choices=MESAS_CHOICES)
  status = models.IntegerField(choices=STATUS_PEDIDO_CHOICES)

  def get_total_pedido(self):
    return self.itens_pedido.aggregate(total_pedido=Coalesce(Sum('valor'), Decimal(0)))['total_pedido']

  def __str__(self):
    return ' '.join(['#Pedido', str(self.id), 'Mesa',str(self.mesa)])

class Estoque(models.Model):
    quantidade = models.IntegerField()
    status = models.BooleanField(choices=STATUS_CHOICES)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    validade = models.DateField()

class ItemPedido(models.Model):
  prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
  pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE, related_name="itens_pedido")
  quantidade = models.IntegerField()
  valor = models.DecimalField(max_digits=5, decimal_places=2)

  def __str__(self):
    return '#Pedido '+str(self.pedido.id)