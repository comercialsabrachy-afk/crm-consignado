from django.contrib import admin
from .models import Convenio, Produto, ConvenioProduto


@admin.register(Convenio)
class ConvenioAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "ativo")
    search_fields = ("nome",)


@admin.register(Produto)
class ProdutoAdmin(admin.ModelAdmin):
    list_display = ("id", "nome", "ativo")
    search_fields = ("nome",)


@admin.register(ConvenioProduto)
class ConvenioProdutoAdmin(admin.ModelAdmin):
    list_display = ("convenio", "produto")
    list_filter = ("convenio", "produto")