from django import forms
from .models import *

class CategoriaForm(forms.ModelForm):
    class Meta:
        model = Categoria
        fields = ['nome', 'ordem']
        widgets = {
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'ordem':forms.NumberInput(attrs={'class': 'inteiro form-control', 'placeholder': ''}),
        }

class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = ['nome', 'cpf', 'datanasc']
        widgets = {
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'cpf':forms.TextInput(attrs={'class': 'cpf form-control', 'placeholder': 'C.P.F'}),
            'datanasc': forms.DateInput(attrs={'class': 'data form-control', 'placeholder': 'Data de Nascimento'}, format='%d/%m/%Y'),
        }

class ProdutoForm(forms.ModelForm):
    class Meta:
        model = Produto
        fields = ['nome', 'preco', 'categoria','img_base64']
        widgets = {
            #'categoria': forms.Select(attrs={'class': 'form-control'}),
            'categoria': forms.HiddenInput(), #Campo oculto para armazenar apenas para o ID
            'nome':forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nome'}),
            'img_base64': forms.HiddenInput(), 
            # a classe money mascara a entreda de valores monetários, está em base.html
            #  jQuery Mask Plugin
            'preco':forms.TextInput(attrs={
                'class': 'money form-control',
                'maxlength': 500,
                'placeholder': '0.000,00'
            }),
        }
        
        labels = {
            'nome': 'Nome do Produto',
            'preco': 'Preço do Produto',
        }


    def __init__(self, *args, **kwargs):
        super(ProdutoForm, self).__init__(*args, **kwargs)
        self.fields['preco'].localize = True
        self.fields['preco'].widget.is_localized = True  

class EstoqueForm(forms.ModelForm):
    class Meta:
        model = Estoque
        fields = ['produto', 'qtde']

        widgets = {
            'produto': forms.HiddenInput(),
            'qtde': forms.TextInput(attrs={'class': 'inteiro form-control',}),
        }

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido
        fields = ['cliente']
        widgets = {
            'cliente': forms.HiddenInput(),  # Campo oculto para armazenar o ID
        }

class ItemPedidoForm(forms.ModelForm):
    class Meta:
        model = ItemPedido
        fields = ['pedido','produto', 'qtde']


        widgets = {
            'pedido': forms.HiddenInput(),  # Campo oculto para armazenar o ID
            'produto': forms.HiddenInput(),  # Campo oculto para armazenar o ID
            'qtde':forms.TextInput(attrs={'class': 'form-control',}),
        }

class PagamentoForm(forms.ModelForm):
     class Meta:
          model = Pagamento
          fields = ['pedido', 'forma', 'valor']
          widgets = {
               'pedido': forms.HiddenInput(),
               'forma': forms.Select(attrs={'class': 'form-control'}),
               'valor': forms.TextInput(attrs={
                    'class': 'money form-control',
                    'maxlenght': '500',
                    'placeholder': '0.000,00',
            }),
         }
     
     def __init__(self, *args, **kwargs):
          super(PagamentoForm, self).__init__(*args, **kwargs)
          self.fields['valor'].localize = True 
          self.fields['valor'].widget.is_localized = True 

     
     def clean_valor(self):
        valor = self.cleaned_data.get('valor')
        pedido = self.cleaned_data.get('pedido')

        if valor <= 0:
            raise forms.ValidationError("O valor deve ser maior que zero.")

        if pedido:
            debito = pedido.debito  # Obtém o valor do débito do pedido
            if valor > debito:
                raise forms.ValidationError("O valor do pagamento não pode ser maior que o débito do pedido.")

        return valor


