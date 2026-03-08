from django import forms
from .models import Oportunidade

class OportunidadeForm(forms.ModelForm):
    class Meta:
        model = Oportunidade
        fields = ["cliente", "convenio", "produto", "responsavel", "proximo_contato"]
        widgets = {
            "cliente": forms.Select(attrs={"class": "form-select"}),
            "convenio": forms.Select(attrs={"class": "form-select"}),
            "produto": forms.Select(attrs={"class": "form-select"}),
            "responsavel": forms.Select(attrs={"class": "form-select"}),
            "proximo_contato": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }