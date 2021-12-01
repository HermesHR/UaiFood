from django import forms
from pedidos.models import MESAS_CHOICES, STATUS_PEDIDO_CHOICES, FORMA_PAGTO_CHOICES, ItemPedido, Pedido, Prato, Caixa
from django.forms.models import inlineformset_factory

class PedidoForm(forms.ModelForm):
  mesa = forms.ChoiceField(label='Mesa', choices=MESAS_CHOICES, widget=forms.Select(attrs={'class': "form-control"}))
  status = forms.ChoiceField(label='Status', choices=STATUS_PEDIDO_CHOICES, widget=forms.Select(attrs={'class': "form-control"}))
  
  class Meta:
    model = Pedido
    fields = ['mesa', 'status']
    
class ItemPedidoForm(forms.ModelForm):
  prato = forms.ModelChoiceField(label='Prato', queryset=Prato.objects.all(), widget=forms.Select(attrs={'class': "form-control"}))
  quantidade = forms.IntegerField(widget=forms.NumberInput(attrs={'class': 'form-control'}))
  
  class Meta:
    model = ItemPedido
    fields = ['prato', 'quantidade']
    
    
FormSetItemPedido = inlineformset_factory(
  Pedido, ItemPedido, form=ItemPedidoForm, extra=0, can_delete=True,
  min_num=0, validate_min=True
) 

class PagamentoForm(forms.ModelForm):
  pagamento = forms.ChoiceField(label='Forma de Pagamento', choices=FORMA_PAGTO_CHOICES, widget=forms.Select(attrs={'class': "form-control"}))

  class Meta:
    model = Caixa
    fields = ['pagamento']