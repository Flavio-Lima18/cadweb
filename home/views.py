from multiprocessing import context
from django.shortcuts import redirect, render, get_object_or_404
from django.contrib import messages
from .forms import *
from .models import *
from django.http import JsonResponse
from django.apps import apps
from django.contrib.auth.decorators import login_required


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

def teste3 (request):
    return render(request, 'testes/teste3.html')

#views Pedido

def pedido(request):
    lista_pedido = Pedido.objects.all().order_by('-id') # Obtém todos os registros
    return render(request, 'pedido/lista.html', {'lista_pedido': lista_pedido})

def novo_pedido(request,id):
    if request.method == 'GET':
        try:
            cliente = Cliente.objects.get(pk=id)
        except Cliente.DoesNotExist:
            # Caso o registro não seja encontrado, exibe a mensagem de erro
            messages.error(request, 'Registro não encontrado')
            return redirect('cliente')  # Redireciona para a listagem
        # cria um novo pedido com o cliente selecionado
        pedido = Pedido(cliente=cliente)
        form = PedidoForm(instance=pedido)# cria um formulario com o novo pedido
        return render(request, 'pedido/formulario.html',{'form': form,})
    else: # se for metodo post, salva o pedido.
        form = PedidoForm(request.POST)
        if form.is_valid():
            pedido = form.save()
            return redirect('pedido')

def detalhes_pedido(request, id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido')  # Redireciona para a listagem    
    
    if request.method == 'GET':
        itemPedido = ItemPedido(pedido=pedido)
        form = ItemPedidoForm(instance=itemPedido)
    else:
        form = ItemPedidoForm(request.POST)
        # aguardando implementação POST, salvar item
        if form.is_valid():
            if form.is_valid():
                item_pedido = form.save(commit=False)  # commit=False permite modificações antes de salvar
                item_pedido.preco = item_pedido.produto.preco  # Acessando o preço do produto relacionado
                estoque_atual = item_pedido.produto.estoque
            
            # Verificação do estoque
            print (f'Quantidade pedido: {item_pedido.qtde}')
            print (f'Estoque: {estoque_atual.qtde}')
            if item_pedido.qtde > estoque_atual.qtde:
                messages.error(request, 'Estoque insuficiente para este produto')
            else:
                # Decrementando a quantidade do estoque
                estoque_atual.qtde = estoque_atual.qtde - item_pedido.qtde
                item_pedido.produto.estoque.qtde = estoque_atual
                estoque_atual.save()
                item_pedido.save()  # Salvando o item do pedido
                print (f'atualizado: {item_pedido.produto.estoque.qtde}')

                messages.success(request, 'Produto adicionado com sucesso!')
                itemPedido = ItemPedido(pedido=pedido)
                form = ItemPedidoForm(instance=itemPedido)
        else:
            messages.error(request, 'Erro ao adicionar produto')

    
    contexto = {
        'pedido': pedido,
        'form': form,
    }
    return render(request, 'pedido/detalhes.html',contexto )

def editar_pedido(request, id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista_pedido')

    if (request.method == 'POST'):
        form = PedidoForm(request.POST, instance=pedido)
        if form.is_valid():
            produto = form.save()
            listaPedido=[]
            listaPedido.append(produto)
            
            return redirect('lista_pedido')

    else: 
        form = PedidoForm(instance=pedido)
    
    return render(request, 'pedido/formulario.html', {'form':form,})

def remover_pedido(request, id):
    try:
        print(f"Tentando excluir o pedido com ID: {id}")
        pedido = Pedido.objects.get(pk=id)
        
        itens_pedido = ItemPedido.objects.filter(pedido=pedido)
        
        for item in itens_pedido:
            estoque_item = Estoque.objects.get(produto=item.produto)
            estoque_item.qtde += item.qtde  # Adiciona a quantidade de volta ao estoque
            estoque_item.save()  # Salva a atualização no estoque

        print(f"Pedido encontrado: {pedido}")
        pedido.delete()
        messages.success(request, 'Exclusão realizda com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('lista_pedido')
    
    return redirect('lista_pedido')

def remover_item_pedido(request, id):   
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
    # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
    return redirect('detalhes_pedido', id=id)
    
    pedido_id = item_pedido.pedido.id  # Armazena o ID do pedido antes de remover o item
    estoque = item_pedido.produto.estoque  # Obtém o estoque do produto
    estoque.qtde += item_pedido.qtde  # Devolve a quantidade do item ao estoque
    estoque.save()  # Salva as alterações no estoque
    # Remove o item do pedido
    item_pedido.delete()
    messages.success(request, 'Operação realizada com Sucesso')


    # Redireciona de volta para a página de detalhes do pedido
    return redirect('detalhes_pedido', id=pedido_id)
def editar_item_pedido(request, id):
    try:
        item_pedido = ItemPedido.objects.get(pk=id)
    except ItemPedido.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=id)

    pedido = item_pedido.pedido  # Obtém o pedido associado
    produto_anterior = item_pedido.produto  # Guarda o produto antes da edição
    quantidade_anterior = item_pedido.qtde  # Guarda a quantidade antes da edição
    
    if request.method == 'POST':
        form = ItemPedidoForm(request.POST, instance=item_pedido)
        
        if form.is_valid():
            item_pedido = form.save(commit=False)  # Obtém a instância sem salvar ainda
            novo_produto = item_pedido.produto  # Obtém o novo produto selecionado
            nova_quantidade = item_pedido.qtde  # Nova quantidade do item

            # Restaurar o estoque do produto anterior antes da atualização
            produto_anterior_estoque = produto_anterior.estoque
            produto_anterior_estoque.qtde += quantidade_anterior
            produto_anterior_estoque.save()

            # Se for o mesmo produto, apenas atualizar a quantidade
            if produto_anterior == novo_produto:
                if produto_anterior_estoque.qtde >= nova_quantidade:
                    produto_anterior_estoque.qtde -= nova_quantidade
                    produto_anterior_estoque.save()
                    item_pedido.save()
                    messages.success(request, 'Item atualizado com sucesso!')
                else:
                    messages.error(request, 'Quantidade insuficiente no estoque!')
                    return redirect('detalhes_pedido', id=pedido.id)
            else:
                # Caso o produto tenha sido alterado, atualizar o estoque do novo produto
                novo_produto_estoque = novo_produto.estoque

                if novo_produto_estoque.qtde >= nova_quantidade:
                    novo_produto_estoque.qtde -= nova_quantidade
                    novo_produto_estoque.save()
                    
                    # Salvar o item do pedido atualizado
                    item_pedido.save()
                    messages.success(request, 'Produto alterado e estoque atualizado!')
                else:
                    messages.error(request, 'Estoque insuficiente para o novo produto!')
                    return redirect('detalhes_pedido', id=pedido.id)

            return redirect('detalhes_pedido', id=pedido.id)
    else:
        form = ItemPedidoForm(instance=item_pedido)
    
    contexto = {
        'pedido': pedido,
        'form': form,
        'item_pedido': item_pedido,
    }
    return render(request, 'pedido/detalhes.html', contexto)

def form_pagamento(request,id):
    try:
        pedido = Pedido.objects.get(pk=id)
    except Pedido.DoesNotExist:
        # Caso o registro não seja encontrado, exibe a mensagem de erro
        messages.error(request, 'Registro não encontrado')
        return redirect('pedido')  # Redireciona para a listagem    
    
    if request.method == 'POST':
        form = PagamentoForm(request.POST)
        if form.is_valid():
            form.save()
            
            messages.success(request, 'Operação realizada com Sucesso')

            pagamento = Pagamento(pedido=pedido)
            form = PagamentoForm(instance=pagamento)
    else: 
        pagamento = Pagamento(pedido=pedido)
        form = PagamentoForm(instance=pagamento)
        
        
    # prepara o formulário para um novo pagamento

    contexto = {
        'pedido': pedido,
        'form': form,
    }    
    return render(request, 'pedido/pagamento.html',contexto)

def remover_pagamento(request, id):
    try:
        pagamento = Pagamento.objects.get(pk=id)
        pedido_id = pagamento.pedido.id
        pagamento.delete()
        messages.success(request, 'Exclusão realizada com Sucesso.')
    except:
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=pedido_id)
    
    return redirect('detalhes_pedido', id=pedido_id)

def editar_pagamento(request, id):
    try:
        pagamento = Pagamento.objects.get(pk=id)
    except Pagamento.DoesNotExist:
        messages.error(request, 'Registro não encontrado')
        return redirect('detalhes_pedido', id=pagamento.pedido.id)

    if request.method == 'POST':
        form = PagamentoForm(request.POST, instance=pagamento)
        if form.is_valid():
            form.save()
            messages.success(request, 'Pagamento atualizado com sucesso!')
            return redirect('detalhes_pedido', id=pagamento.pedido.id)
    else:
        form = PagamentoForm(instance=pagamento)
    
    contexto = {
        'pedido': pagamento.pedido,
        'form': form,
        'pagamento': pagamento,
    }
    return render(request, 'pedido/pagamento.html', contexto)

def nota_fiscal(request, pedido_id):
    pedido = Pedido.objects.get(pk=pedido_id)
    contexto = {
        'pedido': pedido,
    }
    return render(request, 'pedido/nota_fiscal.html', contexto)
