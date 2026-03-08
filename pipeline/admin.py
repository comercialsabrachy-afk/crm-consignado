from django.contrib import admin
from .models import Oportunidade


@admin.register(Oportunidade)
class OportunidadeAdmin(admin.ModelAdmin):
    list_display = ("cliente", "produto", "etapa", "responsavel")
    list_filter = ("etapa", "produto")