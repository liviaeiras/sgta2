from django.urls import path
from . import views

urlpatterns = [
    path('tarefas/', views.listar_tarefas),
    path('tarefas/prioridade/<str:prioridade>/', views.tarefas_por_prioridade),
    path('tarefas/urgentes/', views.tarefas_abertas_urgentes),
    path('tarefas/atrasadas/', views.tarefas_atrasadas),
    path('tarefas/busca/<str:palavra>/', views.buscar_por_titulo),
    path('tarefas/<int:id>/', views.tarefa_por_id),
]