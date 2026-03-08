from django import forms
from .models import Cliente, Telefone


class ClienteForm(forms.ModelForm):
    class Meta:
        model = Cliente
        fields = [
            "nome",
            "cpf",
            "email",
            "data_nascimento",
            "endereco",
            "cidade",
            "observacoes",
            "convenio_principal",
            "nao_contatar",
        ]
        widgets = {
            "nome": forms.TextInput(attrs={"class": "form-control"}),
            "cpf": forms.TextInput(attrs={"class": "form-control"}),
            "email": forms.EmailInput(attrs={"class": "form-control"}),
            "data_nascimento": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "endereco": forms.TextInput(attrs={"class": "form-control"}),
            "cidade": forms.TextInput(attrs={"class": "form-control"}),
            "observacoes": forms.Textarea(attrs={"class": "form-control", "rows": 4}),
            "convenio_principal": forms.Select(attrs={"class": "form-select"}),
            "nao_contatar": forms.CheckboxInput(attrs={"class": "form-check-input"}),
        }


class DoisTelefonesForm(forms.Form):
    numero1 = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    status1 = forms.ChoiceField(
        required=False,
        choices=Telefone.STATUS,
        widget=forms.Select(attrs={"class": "form-select"})
    )

    numero2 = forms.CharField(required=False, widget=forms.TextInput(attrs={"class": "form-control"}))
    status2 = forms.ChoiceField(
        required=False,
        choices=Telefone.STATUS,
        widget=forms.Select(attrs={"class": "form-select"})
    )