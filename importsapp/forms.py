from django import forms

class ImportExcelForm(forms.Form):
    arquivo = forms.FileField(
        label="Arquivo Excel"
    )