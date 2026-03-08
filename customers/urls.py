from django.urls import path
from .views import cliente_list, cliente_create, cliente_detail, cliente_update, cliente_delete

urlpatterns = [
    path("", cliente_list, name="cliente_list"),
    path("novo/", cliente_create, name="cliente_create"),
    path("<int:cliente_id>/", cliente_detail, name="cliente_detail"),
    path("<int:cliente_id>/editar/", cliente_update, name="cliente_update"),
    path("<int:cliente_id>/excluir/", cliente_delete, name="cliente_delete"),
]