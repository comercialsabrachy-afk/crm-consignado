from django.urls import path
from .views import importar_excel

urlpatterns = [
    path("", importar_excel, name="importar_excel"),
]