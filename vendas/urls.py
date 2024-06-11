from . import  views
from django.urls import path
from reciclagem.models import Produto, Categoria, Imagem 





urlpatterns = [

    path('venda_produto/',views.venda_produto, name="venda_produto"),
    path('vender/',views.vender, name="vender"),
     path('vender/<slug:slug>/',views.vender, name="vender"),
    
]