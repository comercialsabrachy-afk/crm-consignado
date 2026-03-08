from django.shortcuts import render, redirect, get_object_or_404
from .models import Cliente, Telefone
from .forms import ClienteForm, DoisTelefonesForm


def cliente_list(request):
    clientes = Cliente.objects.all().prefetch_related("telefones").order_by("-criado_em")
    return render(request, "customers/cliente_list.html", {"clientes": clientes})


def cliente_create(request):
    if request.method == "POST":
        form = ClienteForm(request.POST)
        telefones_form = DoisTelefonesForm(request.POST)

        if form.is_valid() and telefones_form.is_valid():
            cliente = form.save()

            numero1 = telefones_form.cleaned_data.get("numero1")
            status1 = telefones_form.cleaned_data.get("status1")

            numero2 = telefones_form.cleaned_data.get("numero2")
            status2 = telefones_form.cleaned_data.get("status2")

            if numero1:
                Telefone.objects.create(
                    cliente=cliente,
                    numero=numero1,
                    status=status1 or "VALIDO"
                )

            if numero2:
                Telefone.objects.create(
                    cliente=cliente,
                    numero=numero2,
                    status=status2 or "VALIDO"
                )

            return redirect("cliente_list")
    else:
        form = ClienteForm()
        telefones_form = DoisTelefonesForm()

    return render(request, "customers/cliente_form.html", {
        "form": form,
        "telefones_form": telefones_form,
        "modo": "novo"
    })


def cliente_detail(request, cliente_id):
    cliente = get_object_or_404(
        Cliente.objects.prefetch_related("telefones", "oportunidades"),
        id=cliente_id
    )
    telefones = cliente.telefones.all()
    oportunidades = cliente.oportunidades.all().order_by("-criado_em")

    return render(request, "customers/cliente_detail.html", {
        "cliente": cliente,
        "telefones": telefones,
        "oportunidades": oportunidades,
    })


def cliente_update(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)
    telefones = list(cliente.telefones.all()[:2])

    initial_telefones = {
        "numero1": telefones[0].numero if len(telefones) > 0 else "",
        "status1": telefones[0].status if len(telefones) > 0 else "VALIDO",
        "numero2": telefones[1].numero if len(telefones) > 1 else "",
        "status2": telefones[1].status if len(telefones) > 1 else "VALIDO",
    }

    if request.method == "POST":
        form = ClienteForm(request.POST, instance=cliente)
        telefones_form = DoisTelefonesForm(request.POST)

        if form.is_valid() and telefones_form.is_valid():
            form.save()

            cliente.telefones.all().delete()

            numero1 = telefones_form.cleaned_data.get("numero1")
            status1 = telefones_form.cleaned_data.get("status1")

            numero2 = telefones_form.cleaned_data.get("numero2")
            status2 = telefones_form.cleaned_data.get("status2")

            if numero1:
                Telefone.objects.create(
                    cliente=cliente,
                    numero=numero1,
                    status=status1 or "VALIDO"
                )

            if numero2:
                Telefone.objects.create(
                    cliente=cliente,
                    numero=numero2,
                    status=status2 or "VALIDO"
                )

            return redirect("cliente_detail", cliente_id=cliente.id)
    else:
        form = ClienteForm(instance=cliente)
        telefones_form = DoisTelefonesForm(initial=initial_telefones)

    return render(request, "customers/cliente_form.html", {
        "form": form,
        "telefones_form": telefones_form,
        "cliente": cliente,
        "modo": "editar"
    })


def cliente_delete(request, cliente_id):
    cliente = get_object_or_404(Cliente, id=cliente_id)

    if request.method == "POST":
        cliente.delete()
        return redirect("cliente_list")

    return render(request, "customers/cliente_delete.html", {
        "cliente": cliente
    })