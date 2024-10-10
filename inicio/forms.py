from django import forms

class CrearComputadoraFormulario(forms.Form):
    cpu = forms.CharField(max_length=15)
    gpu = forms.CharField(max_length=15)
    ram = forms.IntegerField()

class BuscarComputadoraFormulario(forms.Form):
    cpu = forms.CharField(max_length=15, required=False)
    