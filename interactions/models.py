from django.db import models


class Interacao(models.Model):
    RESULTADOS = (
        ("ENVIADA", "Mensagem enviada"),
        ("RECEBIDA", "Recebida"),
        ("SEM_RESPOSTA", "Sem resposta"),
        ("NEGOCIANDO", "Negociando"),
        ("FECHADO", "Fechado"),
        ("PERDIDO", "Perdido"),
        ("BLOQUEADO", "Bloqueado"),
    )

    oportunidade = models.ForeignKey(
        "pipeline.Oportunidade",
        on_delete=models.CASCADE,
        related_name="interacoes"
    )

    resultado = models.CharField(max_length=20, choices=RESULTADOS)
    descricao = models.TextField(blank=True)
    ocorrido_em = models.DateTimeField(auto_now_add=True)
    proximo_contato = models.DateField(null=True, blank=True)

    def __str__(self):
        return f"{self.oportunidade} - {self.resultado}"