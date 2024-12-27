from django import forms
from .models import Gasto, Departamento, Empleado

class GastoForm(forms.ModelForm):
    class Meta:
        model = Gasto
        fields = ['fecha', 'descripcion', 'monto', 'empleado', 'departamento']


class DepartamentoForm(forms.ModelForm):
    class Meta:
        model = Departamento
        fields = ['nombre']

class EmpleadoForm(forms.ModelForm):
    class Meta:
        model = Empleado
        fields = ['nombre', 'departamento']

class FechaFilterForm(forms.Form):
    fecha_inicio = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Fecha Inicio'
    )
    fecha_fin = forms.DateField(
        widget=forms.DateInput(attrs={'type': 'date'}),
        label='Fecha Fin'
    )

