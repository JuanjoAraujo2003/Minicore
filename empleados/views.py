from django.shortcuts import render, redirect
from .models import Gasto, Empleado, Departamento
from .forms import GastoForm, EmpleadoForm, DepartamentoForm, FechaFilterForm
from django.db.models import Sum, DecimalField
from django.db.models.functions import Coalesce

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


def gastos_por_departamento(request):
    form = FechaFilterForm(request.GET or None)
    resultados = []

    if form.is_valid():
        fecha_inicio = form.cleaned_data['fecha_inicio']
        fecha_fin = form.cleaned_data['fecha_fin']

        # Obtener todos los departamentos y calcular sus gastos
        departamentos = Departamento.objects.all()

        for depto in departamentos:
            total_gastos = Gasto.objects.filter(
                empleado__departamento=depto,
                fecha__gte=fecha_inicio,
                fecha__lte=fecha_fin
            ).aggregate(
                total=Coalesce(Sum('monto'), 0.00,  output_field=DecimalField(max_digits=10, decimal_places=2))
            )['total']

            resultados.append({
                'departamento': depto.nombre,
                'total': total_gastos
            })

    return render(request, 'empleados/filtrado.html', {
        'form': form,
        'resultados': resultados
    })




