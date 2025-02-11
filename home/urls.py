from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    #Categoria
    path('categoria/lista', views.categoria, name="lista"),
    path('categoria/formulario', views.form_categoria, name="form_categoria"),
    path('editar_categoria/<int:id>', views.editar_categoria, name="editar_categoria"),
    path('detalhes_categoria/<int:id>', views.detalhes_categoria, name="detalhes_categoria"),
    path('remover_categoria/<int:id>', views.remover_categoria, name="remover_categoria"),
    #Cliente
    path('cliente/lista', views.cliente, name="lista_cliente"),
    path('cliente/formulario', views.form_cliente, name="form_cliente"),
    path('editar_cliente/<int:id>', views.editar_cliente, name="editar_cliente"),
    path('detalhes_cliente/<int:id>', views.detalhes_cliente, name="detalhes_cliente"),
    path('remover_cliente/<int:id>', views.remover_cliente, name="remover_cliente"),
    #Produto
    path('produto/lista', views.produto, name="lista_produto"),
    path('produto/formulario', views.form_produto, name="form_produto"),
    path('editar_produto/<int:id>', views.editar_produto, name="editar_produto"),
    path('detalhes_produto/<int:id>', views.detalhes_produto, name="detalhes_produto"),
    path('remover_produto/<int:id>', views.remover_produto, name="remover_produto"),
    #Estoque
    path('ajustar_estoque/<int:id>', views.ajustar_estoque, name="ajustar_estoque"),

]