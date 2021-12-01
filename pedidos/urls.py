from django.urls import path

from . import views

urlpatterns = [
  path('', views.index, name='index'),
  path('cardapio/', views.cardapio, name='cardapio'),
  path('mesas/', views.mesas, name='mesas'),
  path('lista_pedidos/', views.lista_pedidos, name='lista_pedidos'),
  path('form_pedido/', views.form_pedido, name='form_pedido'),
  path('atualizar_pedido/<int:pk>/', views.atualizar_pedido, name='atualizar_pedido'),
  path('deletar_pedido/<int:pk>/', views.deletar_pedido, name='deletar_pedido'),
  path('financeiro/', views.financeiro, name='financeiro'),
  path('pagamento/<int:pk>/', views.pagamento, name='pagamento'),
  path('atualizar_status/', views.atualizar_status, name='atualizar_status')
]