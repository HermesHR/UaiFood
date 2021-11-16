from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('cardapio/', views.cardapio, name='cardapio'),
  path('mesas/', views.mesas, name='mesas'),
  path('enviapedido/', views.enviapedido, name='enviapedido')
]

