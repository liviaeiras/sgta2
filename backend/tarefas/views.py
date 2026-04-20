from django.shortcuts import render

# Create your views here
from django.http import JsonResponse
from .models import Tarefa

# Ex. 1 da Aula 6 — todas as tarefas
def listar_tarefas(request):
    tarefas = Tarefa.objects.all().values()
    return JsonResponse(list(tarefas), safe=False)

# Ex. 2 — filtrar por prioridade
def tarefas_por_prioridade(request, prioridade):
    tarefas = Tarefa.objects.filter(prioridade=prioridade).values()
    return JsonResponse(list(tarefas), safe=False)

# Ex. 3 — buscar por id
def tarefa_por_id(request, id):
    try:
        tarefa = Tarefa.objects.get(pk=id)
        return JsonResponse({
            'id': tarefa.id,
            'titulo': tarefa.titulo,
            'status': tarefa.status,
            'prioridade': tarefa.prioridade,
        })
    except Tarefa.DoesNotExist:
        return JsonResponse({'erro': 'Tarefa não encontrada.'}, status=404)

# Ex. 4 — abertas e urgentes
def tarefas_abertas_urgentes(request):
    tarefas = Tarefa.objects.filter(status='ABERTA', prioridade='URGENTE').values()
    return JsonResponse(list(tarefas), safe=False)

# Ex. 5 — tarefas atrasadas
from django.utils import timezone

def tarefas_atrasadas(request):
    hoje = timezone.now().date()
    tarefas = Tarefa.objects.filter(
        data_entrega__lt=hoje
    ).exclude(status='CONCLUIDA').values()
    return JsonResponse(list(tarefas), safe=False)

# Ex. 6 — buscar por palavra no título
def buscar_por_titulo(request, palavra):
    tarefas = Tarefa.objects.filter(titulo__icontains=palavra).values()
    return JsonResponse(list(tarefas), safe=False)
