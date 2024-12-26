from django.urls import path
from . import views

urlpatterns = [
    path('', views.lista_gastos, name='lista_gastos'),
    path('agregar/', views.agregar_gasto, name='agregar_gasto'),
    path('departamentos/', views.lista_departamentos, name='lista_departamentos'),
    path('departamentos/agregar/', views.agregar_departamento, name='agregar_departamentos'),
    path('empleados/', views.lista_empleados, name='lista_empleados'),
    path('empleados/agregar/', views.agregar_empleado, name='agregar_empleado'),
    path('gastos_por_departamento/', views.gastos_por_departamento, name='gastos_por_departamento'),

]