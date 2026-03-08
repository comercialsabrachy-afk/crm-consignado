from django.contrib import admin
from .models import Cliente, Telefone


@admin.register(Cliente)
class ClienteAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "cpf", "convenio_principal")
    search_fields = ("nome", "cpf")


@admin.register(Telefone)
class TelefoneAdmin(admin.ModelAdmin):
    list_display = ("numero", "cliente", "status")
    list_filter = ("status",)
