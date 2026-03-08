from django.db import models
from pipeline.models import Oportunidade

class Tarefa(models.Model):
    STATUS = (
        ("PENDENTE", "Pendente"),
        ("FEITA", "Feita"),
    )

    oportunidade = models.ForeignKey(Oportunidade, on_delete=models.CASCADE)
    titulo = models.CharField(max_length=120)
    agendada_para = models.DateTimeField()
    status = models.CharField(max_length=20, choices=STATUS, default="PENDENTE")