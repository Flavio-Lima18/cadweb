from django.shortcuts import redirect, render
from django.contrib import messages
from .forms import *
from .models import *

def index(request):
    return render(request,'index.html')

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