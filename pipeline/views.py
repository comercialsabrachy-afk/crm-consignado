from django.shortcuts import render, redirect, get_object_or_404
from .models import Oportunidade
from .forms import OportunidadeForm


def kanban(request):
    colunas = [
        ("SEM", "Sem atendimento", "secondary"),
        ("ATEND", "Em atendimento", "primary"),
        ("NEG", "Negociação", "warning"),
        ("GANHO", "Fechado", "success"),
        ("PERD", "Perdido", "danger"),
    ]

    kanban_data = []

    for codigo, nome, cor in colunas:
        oportunidades = (
            Oportunidade.objects
            .select_related("cliente", "convenio", "produto", "responsavel")
            .filter(etapa=codigo)
            .order_by("-criado_em")
        )

        kanban_data.append({
            "codigo": codigo,
            "nome": nome,
            "cor": cor,
            "total": oportunidades.count(),
            "cards": oportunidades,
        })

    total_geral = Oportunidade.objects.count()

    return render(request, "pipeline/kanban.html", {
        "kanban_data": kanban_data,
        "total_geral": total_geral,
    })


def nova_oportunidade(request):
    cliente_id = request.GET.get("cliente")

    if request.method == "POST":
        form = OportunidadeForm(request.POST)
        if form.is_valid():
            oportunidade = form.save()
            return redirect("detalhe_oportunidade", oportunidade_id=oportunidade.id)
    else:
        initial = {}
        if cliente_id:
            initial["cliente"] = cliente_id
        form = OportunidadeForm(initial=initial)

    return render(request, "pipeline/nova_oportunidade.html", {"form": form})


def detalhe_oportunidade(request, oportunidade_id):
    oportunidade = get_object_or_404(
        Oportunidade.objects.select_related("cliente", "convenio", "produto", "responsavel"),
        id=oportunidade_id
    )

    interacoes = oportunidade.interacoes.all().order_by("-ocorrido_em")

    return render(request, "pipeline/detalhe_oportunidade.html", {
        "oportunidade": oportunidade,
        "interacoes": interacoes,
    })