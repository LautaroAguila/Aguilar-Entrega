from django import forms


class CompuFormularioBase(forms.Form):
    cpu = forms.CharField(max_length=15)
    gpu = forms.CharField(max_length=15)
    ram = forms.IntegerField()

class CrearComputadoraFormulario(CompuFormularioBase):...

class BuscarComputadoraFormulario(forms.Form):
    cpu = forms.CharField(max_length=15, required=False)
    
class EditarComputadoraFormulario(CompuFormularioBase):...