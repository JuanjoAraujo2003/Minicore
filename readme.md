# Minicore 
# Autor: Juan Araujo

## Descripción
Minicore es una aplicación web desarrollada con Django que permite gestionar los empleados y departamentos de una empresa. Su principal funcionalidad incluye:

- Crear, editar y eliminar empleados.
- Crear y gestionar departamentos.
- Generar gastos asociados a departamentos por empleados que formen parte de ellos.
- Filtrar los gastos realizados dentro de un rango de fechas, mostrando los gastos organizados por departamento.

Es una herramienta diseñada para facilitar la gestión interna de los recursos de una empresa.

---

## Pasos para Configurar y Usar Minicore

### 1. Clonar el Repositorio
Clona el repositorio en tu máquina local:
```bash
git clone https://github.com/usuario/minicore.git
cd minicore
```
### 2. Crear un Entorno Virtual
Crea un entorno virtual para instalar las dependencias del proyecto:
```bash
python -m venv venv
source venv/bin/activate
```
### 3. Instalar Dependencias
Instala las dependencias del proyecto:
```bash
pip install -r requirements.txt
```
### 4. Crear la Base de Datos
Crea la base de datos y aplica las migraciones:
```bash
python ,anage.py makemigrations
python manage.py migrate
```
### 5. Crear un Superusuario
Crea un superusuario para acceder al panel de administración:
```bash
python manage.py createsuperuser
```
### 6. Ejecutar el Servidor
Ejecuta el servidor de desarrollo:
```bash
python manage.py runserver
```
### 7. Siguiendo estos pasos podras ejecutar la aplicacion en tu maquina :D
