from django import forms
from .models import Interacao

class InteracaoForm(forms.ModelForm):
    class Meta:
        model = Interacao
        fields = ["resultado", "descricao", "proximo_contato"]
        widgets = {
            "resultado": forms.Select(attrs={"class": "form-select"}),
            "descricao": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "proximo_contato": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }