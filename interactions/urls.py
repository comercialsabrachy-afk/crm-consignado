from django.urls import path
from .views import nova_interacao

urlpatterns = [
    path("nova/<int:oportunidade_id>/", nova_interacao, name="nova_interacao"),
]