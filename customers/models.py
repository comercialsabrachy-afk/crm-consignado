from django.db import models
from core.models import Convenio


class Cliente(models.Model):
    nome = models.CharField(max_length=150)
    cpf = models.CharField(max_length=11, unique=True)
    email = models.EmailField(blank=True, null=True)

    data_nascimento = models.DateField(blank=True, null=True)
    endereco = models.CharField(max_length=200, blank=True, null=True)
    cidade = models.CharField(max_length=100, blank=True, null=True)
    observacoes = models.TextField(blank=True, null=True)

    convenio_principal = models.ForeignKey(Convenio, on_delete=models.PROTECT)

    nao_contatar = models.BooleanField(default=False)
    criado_em = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.nome


class Telefone(models.Model):
    STATUS = (
        ("VALIDO", "Válido"),
        ("INVALIDO", "Inválido"),
        ("BLOQUEADO", "Bloqueado"),
    )

    cliente = models.ForeignKey(Cliente, on_delete=models.CASCADE, related_name="telefones")
    numero = models.CharField(max_length=20)
    status = models.CharField(max_length=10, choices=STATUS, default="VALIDO")

    def __str__(self):
        return self.numero