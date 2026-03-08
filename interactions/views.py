from django.shortcuts import render, redirect, get_object_or_404
from .forms import InteracaoForm
from .models import Interacao
from pipeline.models import Oportunidade

def nova_interacao(request, oportunidade_id):
    oportunidade = get_object_or_404(Oportunidade, id=oportunidade_id)

    if request.method == "POST":
        form = InteracaoForm(request.POST)
        if form.is_valid():
            interacao = form.save(commit=False)
            interacao.oportunidade = oportunidade
            interacao.save()

            # Atualiza etapa automaticamente conforme resultado
            if interacao.resultado == "ENVIADA":
                oportunidade.etapa = "ATEND"
            elif interacao.resultado in ["RECEBIDA", "NEGOCIANDO"]:
                oportunidade.etapa = "NEG"
            elif interacao.resultado == "FECHADO":
                oportunidade.etapa = "GANHO"
            elif interacao.resultado in ["PERDIDO", "BLOQUEADO"]:
                oportunidade.etapa = "PERD"

            oportunidade.save()
            return redirect("detalhe_oportunidade", oportunidade_id=oportunidade.id)
    else:
        form = InteracaoForm()

    return render(request, "interactions/nova_interacao.html", {
        "form": form,
        "oportunidade": oportunidade
    })