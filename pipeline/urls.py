from django.urls import path
from .views import kanban, nova_oportunidade, detalhe_oportunidade

urlpatterns = [
    path("", kanban, name="kanban"),
    path("oportunidades/nova/", nova_oportunidade, name="nova_oportunidade"),
    path("oportunidades/<int:oportunidade_id>/", detalhe_oportunidade, name="detalhe_oportunidade"),
]