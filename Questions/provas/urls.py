from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('exibir_prova/<int:prova_id>/', views.exibir_prova, name='exibir_prova'),
    path('resultados/', views.resultados_prova, name='resultados_prova'),
    path('excluir-pergunta/<int:pergunta_id>/', views.excluir_pergunta, name='excluir_pergunta'),
]
