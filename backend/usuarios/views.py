from django.http import JsonResponse
from .models import Usuario

def listar_usuarios(request):
    usuarios = Usuario.objects.all()

    data = []
    for u in usuarios:
        data.append({
            'id': u.id,
            'nome': u.nome,
            'email': u.email,
            'ativo': u.ativo,
            'data_criacao': u.data_criacao,
        })

    return JsonResponse(data, safe=False)