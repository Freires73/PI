from django.urls import path
from . import views

urlpatterns = [

    path('add_produto/', views.add_produto, name="add_produto"),
   
    path('excluir_produto/<str:id>/',views.excluir_produto, name="excluir_produto"),
]