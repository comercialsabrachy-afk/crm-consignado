from django.db import models
from django.contrib.auth import get_user_model


class Oportunidade(models.Model):
    ETAPAS = (
        ("SEM", "Sem atendimento"),
        ("ATEND", "Em atendimento"),
        ("NEG", "Negociação"),
        ("GANHO", "Fechado"),
        ("PERD", "Perdido"),
        ("BLOQ", "Bloqueado"),
    )

    cliente = models.ForeignKey("customers.Cliente", on_delete=models.CASCADE)
    convenio = models.ForeignKey("core.Convenio", on_delete=models.PROTECT)
    produto = models.ForeignKey("core.Produto", on_delete=models.PROTECT)

    etapa = models.CharField(max_length=10, choices=ETAPAS, default="SEM")
    responsavel = models.ForeignKey(get_user_model(), on_delete=models.PROTECT)

    proximo_contato = models.DateTimeField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)
    from django.db import models
from django.contrib.auth import get_user_model
from core.models import Convenio, Produto

User = get_user_model()

class Oportunidade(models.Model):
    ETAPAS = (
        ("SEM", "Sem atendimento"),
        ("ATEND", "Em atendimento"),
        ("NEG", "Negociação"),
        ("GANHO", "Fechado"),
        ("PERD", "Perdido"),
    )

    cliente = models.ForeignKey("customers.Cliente", on_delete=models.CASCADE, related_name="oportunidades")
    convenio = models.ForeignKey(Convenio, on_delete=models.PROTECT)
    produto = models.ForeignKey(Produto, on_delete=models.PROTECT)
    responsavel = models.ForeignKey(User, on_delete=models.PROTECT)

    etapa = models.CharField(max_length=10, choices=ETAPAS, default="SEM")
    proximo_contato = models.DateField(null=True, blank=True)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.cliente.nome} - {self.produto.nome}"