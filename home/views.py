from multiprocessing import context
from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from .models import *
from django.http import JsonResponse
from django.apps import apps

def index(request):
    return render(request,'index.html')

#urls Categoria

def categoria(request):
   contexto = {
       'lista': Categoria.objects.all().order_by('id'),
   }
   return render(request, 'categoria/lista.html', contexto)

def form_categoria(request, id=None):
    if id:
        try:
            categoria = Categoria.objects.get(pk=id)  
        except Categoria.DoesNotExist:
            messages.error(request, 'Categoria não encontrada.')
            return redirect('lista')
    else:
        categoria = None  

    if request.method == 'POST':
        form = CategoriaForm(request.POST, instance=categoria) 
        if form.is_valid():
            form.save() 
            messages.success(request, 'Operação realizada com sucesso.')
            return redirect('lista')  
        else:
            messages.error(request, 'Erro ao processar o formulário.')
    else:  
        form = CategoriaForm(instance=categoria)  

    return render(request, 'categoria/formulario.html', {'form': form})

def editar_categoria(request, id):
    try: 
        categoria = Categoria.objects.get(pk=id)
    except: 
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')

    if (request.method == 'POST'):
        form = CategoriaForm(request.POST, instance = categoria)
        if form.is_valid():
            categoria = form.save()
            lista=[]
            lista.append(categoria)
            return render(request, 'categoria/lista.html', {'lista':lista})    
    else: 
        form = CategoriaForm(instance = categoria)
        return render(request, 'categoria/formulario.html', {'form': form})
    
def detalhes_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
    except Categoria.DoesNotExist:
        messages.error(request, 'Categoria não encontrada.')
        return redirect('lista')
    
    return render(request, 'categoria/detalhes.html', {'categoria': categoria})


def remover_categoria(request, id):
    try:
        categoria = Categoria.objects.get(pk=id)
        categoria.delete()
        messages.success(request, 'Exclusão realizada com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista')
    
    return redirect('lista')

#urls Cliente

def cliente(request):
   contexto = {
       'lista_cliente': Cliente.objects.all().order_by('id'),
   }
   return render(request, 'cliente/lista.html', contexto)

def form_cliente(request, id=None):
    if id:
        try:
            cliente = Cliente.objects.get(pk=id)  
        except Cliente.DoesNotExist:
            messages.error(request, 'Cliente não encontrado.')
            return redirect('lista_cliente')
    else:
        cliente = None  

    if request.method == 'POST':
        form = ClienteForm(request.POST, instance=cliente) 
        if form.is_valid():
            form.save() 
            messages.success(request, 'Operação realizada com sucesso.')
            return redirect('lista_cliente')  
        else:
            messages.error(request, 'Erro ao processar o formulário.')
    else:  
        form = ClienteForm(instance=cliente)  

    return render(request, 'cliente/formulario.html', {'form': form})

def editar_cliente(request, id):
    try: 
        cliente = Cliente.objects.get(pk=id)
    except: 
        messages.error(request, 'Registro não encontrado')
        return redirect('lista_cliente')

    if (request.method == 'POST'):
        form = ClienteForm(request.POST, instance = cliente)
        if form.is_valid():
            cliente = form.save()
            lista_cliente=[]
            lista_cliente.append(cliente)
            return render(request, 'cliente/lista.html', {'lista_cliente':lista_cliente})    
    else: 
        form = ClienteForm(instance = cliente)
        return render(request, 'cliente/formulario.html', {'form': form})
    
def detalhes_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
    except Cliente.DoesNotExist:
        messages.error(request, 'Cliente não encontrado.')
        return redirect('lista_cliente')
    
    return render(request, 'cliente/detalhes.html', {'cliente': cliente})

def remover_cliente(request, id):
    try:
        cliente = Cliente.objects.get(pk=id)
        cliente.delete()
        messages.success(request, 'Exclusão realizada com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista_cliente')
    
    return redirect('lista_cliente')

# urls Produto

def produto (request):
    contexto = {
          'lista_produto': Produto.objects.all().order_by('id'),
    }
    return render(request, 'produto/lista.html', contexto)

def form_produto(request, id=None):
    if id:
        try:
            produto = Produto.objects.get(pk=id)  
        except Produto.DoesNotExist:
            messages.error(request, 'Produto não encontrado.')
            return redirect('lista_produto')
    else:
        produto = None  

    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance=produto) 
        if form.is_valid():
            form.save() 
            messages.success(request, 'Operação realizada com sucesso.')
            return redirect('lista_produto')  
        else:
            messages.error(request, 'Erro ao processar o formulário.')
    else:  
        form = ProdutoForm(instance=produto)  

    return render(request, 'produto/formulario.html', {'form': form})

def editar_produto(request, id):
    try: 
        produto = Produto.objects.get(pk=id)
    except: 
        messages.error(request, 'Registro não encontrado')
        return redirect('lista_produto')

    if (request.method == 'POST'):
        form = ProdutoForm(request.POST, instance = produto)
        if form.is_valid():
            produto = form.save()
            lista_produto=[]
            lista_produto.append(produto)
            return render(request, 'produto/lista.html', {'lista_produto':lista_produto})    
    else: 
        form = ProdutoForm(instance = produto)
        return render(request, 'produto/formulario.html', {'form': form})

def detalhes_produto(request, id):
    try:
        produto = Produto.objects.get(pk=id)
    except Produto.DoesNotExist:
        messages.error(request, 'Produto não encontrado.')
        return redirect('lista_produto')
    
    return render(request, 'produto/detalhes.html', {'produto': produto})

def remover_produto(request, id): 
    try:
        produto = Produto.objects.get(pk=id)
        produto.delete()
        messages.success(request, 'Exclusão realizada com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista_produto')
    
    return redirect('lista_produto')

#urls Estoque

def ajustar_estoque(request, id):
    produto = Produto.objects.get(pk=id)
    estoque = produto.estoque 
    if request.method == 'POST':
        form = EstoqueForm(request.POST, instance=estoque)
        if form.is_valid():
            estoque = form.save()
            lista_produto = []
            lista_produto.append(estoque.produto) 
            return redirect('lista_produto')
            # return render(request, 'produto/lista.html', {'lista_produto': lista_produto})
    else:
         form = EstoqueForm(instance=estoque)
    return render(request, 'produto/estoque.html', {'form': form,})

#urls Testes 

def teste1 (request):
    return render(request, 'testes/teste1.html')

def teste2 (request):
    return render(request, 'testes/teste2.html')

def buscar_dados(request, app_modelo):
    termo = request.GET.get('q', '') # pega o termo digitado
    try:
        # Divida o app e o modelo
        app, modelo = app_modelo.split('.')
        modelo = apps.get_model(app, modelo)
    except LookupError:
        return JsonResponse({'error': 'Modelo não encontrado'}, status=404)
    
    # Verifica se o modelo possui os campos 'nome' e 'id'
    if not hasattr(modelo, 'nome') or not hasattr(modelo, 'id'):
        return JsonResponse({'error': 'Modelo deve ter campos "id" e "nome"'}, status=400)
    
    resultados = modelo.objects.filter(nome__icontains=termo)
    dados = [{'id': obj.id, 'nome': obj.nome} for obj in resultados]
    return JsonResponse(dados, safe=False)


