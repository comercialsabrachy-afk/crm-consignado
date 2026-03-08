from django.shortcuts import render
from core.models import Convenio
from customers.models import Cliente, Telefone
from .forms import ImportExcelForm
import openpyxl

def importar_excel(request):
    convenios = Convenio.objects.all().order_by("nome")
    resultado = None

    if request.method == "POST":
        form = ImportExcelForm(request.POST, request.FILES)
        convenio_id = request.POST.get("convenio_id")

        if form.is_valid() and convenio_id:
            convenio = Convenio.objects.get(id=convenio_id)
            arquivo = form.cleaned_data["arquivo"]

            wb = openpyxl.load_workbook(arquivo)
            ws = wb.active

            importados = 0
            erros = []

            for i, row in enumerate(ws.iter_rows(min_row=2, values_only=True), start=2):
                nome, cpf, email, tel1, tel2 = (row + (None, None, None, None, None))[:5]

                if not nome or not cpf:
                    erros.append(f"Linha {i}: Nome/CPF vazio")
                    continue

                cpf = str(cpf).replace(".", "").replace("-", "").strip()

                cliente, created = Cliente.objects.get_or_create(
                    cpf=cpf,
                    defaults={
                        "nome": str(nome).strip(),
                        "email": str(email).strip() if email else None,
                        "convenio_principal": convenio
                    }
                )

                if created:
                    importados += 1

                for tel in [tel1, tel2]:
                    if tel:
                        Telefone.objects.get_or_create(cliente=cliente, numero=str(tel).strip())

            resultado = {"importados": importados, "erros": erros}
    else:
        form = ImportExcelForm()

    return render(request, "imports/importar_excel.html", {
        "form": form,
        "convenios": convenios,
        "resultado": resultado
    })

# Create your views here.
