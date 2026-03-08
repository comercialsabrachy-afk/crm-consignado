from django.contrib import admin
from .models import Interacao


@admin.register(Interacao)
class InteracaoAdmin(admin.ModelAdmin):
    list_display = ("oportunidade", "resultado", "ocorrido_em")