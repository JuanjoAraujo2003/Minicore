from django.shortcuts import render, redirect
from .models import Gasto, Empleado, Departamento
from .forms import GastoForm, EmpleadoForm, DepartamentoForm

# Create your views here.

def lista_gastos(request):
    gastos = Gasto.objects.all()
    return render(request, 'empleados/lista_gastos.html', {'gastos': gastos})

def agregar_gasto(request):
    if request.method == 'POST':
        form = GastoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_gastos')
    else:
        form = GastoForm()
    return render(request, 'empleados/agregar_gasto.html', {'form': form})

def lista_departamentos(request):
    departamentos = Departamento.objects.all()
    return render(request, 'empleados/lista_departamentos.html', {'departamentos': departamentos})

def agregar_departamento(request):
    if request.method == 'POST':
        form = DepartamentoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_departamentos')
    else:
        form = DepartamentoForm()
    return render(request, 'empleados/agregar_departamentos.html', {'form': form})


def lista_empleados(request):
    empleados = Empleado.objects.all()
    return render(request, 'empleados/lista_empleados.html', {'empleados': empleados})

def agregar_empleado(request):
    if request.method == 'POST':
        form = EmpleadoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('lista_empleados')
    else:
        form = EmpleadoForm()
    return render(request, 'empleados/agregar_empleado.html', {'form': form})



