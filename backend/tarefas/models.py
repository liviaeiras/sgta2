from django.db import models

# Create your models here

class Tarefa(models.Model):

    STATUS_CHOICES = [
        ('ABERTA', 'Aberta'),
        ('EM_ANDAMENTO', 'Em andamento'),
        ('CONCLUIDA', 'Concluída'),
        ('CANCELADA', 'Cancelada'),
    ]

    PRIORIDADE_CHOICES = [
        ('URGENTE', 'Urgente'),
        ('NAO_URGENTE', 'Não Urgente'),
    ]

    titulo = models.CharField(max_length=255)
    descricao = models.TextField()
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='ABERTA')
    prioridade = models.CharField(max_length=20, choices=PRIORIDADE_CHOICES, default='NAO_URGENTE')
    data_criacao = models.DateTimeField(auto_now_add=True)
    data_entrega = models.DateField()

    def __str__(self):
        return self.titulo
