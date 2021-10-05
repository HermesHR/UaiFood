from django.db import models
from django.contrib.auth.models import User


STATUS_CHOICES = (
      (0, "Não"),
      (1, "Sim")
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

class Pedido(models.Model):
  usuario = models.ForeignKey(User, on_delete=models.CASCADE)
  data = models.DateTimeField(auto_now_add=True)
  quantidade = models.IntegerField()
  total = models.DecimalField(max_digits=5, decimal_places=2)

class Estoque(models.Model):
    quantidade = models.IntegerField()
    status = models.BooleanField(choices=STATUS_CHOICES)
    prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
    criado = models.DateTimeField(auto_now_add=True)
    atualizado = models.DateTimeField(auto_now=True)
    validade = models.DateField()

class ItemPedido(models.Model):
  prato = models.ForeignKey(Prato, on_delete=models.CASCADE)
  pedido = models.ForeignKey(Pedido, on_delete=models.CASCADE)
  quantidade = models.IntegerField()
  valor = models.DecimalField(max_digits=5, decimal_places=2)