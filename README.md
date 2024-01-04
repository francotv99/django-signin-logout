# django-signin-logout
A project about thata can create user sign in, sign out, sign up. And create,edit and eliminate tasks 
# Proyecto Django de Gestión de Tareas

Este es un proyecto Django que proporciona una interfaz para que los usuarios puedan gestionar sus tareas. Incluye las siguientes funcionalidades:

- Crear un nuevo usuario: Los usuarios pueden registrarse proporcionando su nombre de usuario, dirección de correo electrónico y contraseña.
- Iniciar sesión: Los usuarios registrados pueden iniciar sesión con su nombre de usuario y contraseña.
- Crear, editar y eliminar tareas: Una vez que los usuarios han iniciado sesión, pueden crear nuevas tareas, editar las existentes y eliminarlas cuando ya no sean necesarias.

## Requisitos

Para ejecutar este proyecto, necesitarás tener instalado lo siguiente:

- Python 3.x
- Django 3.x

## Configuración

1. Clona este repositorio en tu máquina local.
2. Navega hasta el directorio del proyecto.
3. Crea un entorno virtual: `python -m venv venv`
4. Activa el entorno virtual:
   - Windows: `venv\Scripts\activate`
   - macOS/Linux: `source venv/bin/activate`
5. Instala las dependencias: `pip install django(entre otras)`
6. Ejecuta las migraciones: `python manage.py migrate`
7. Crea un superusuario: `python manage.py createsuperuser`
8. Inicia el servidor de desarrollo: `python manage.py runserver`

## Uso

Una vez que el servidor esté en funcionamiento, puedes acceder a la aplicación en tu navegador web ingresando la dirección `http://localhost:8000/`. Desde allí, podrás registrarte como nuevo usuario, iniciar sesión si ya tienes una cuenta y comenzar a gestionar tus tareas.

## Contribuir

Si quieres contribuir a este proyecto, siéntete libre de hacer un fork y enviar tus pull requests. Cualquier aporte es bienvenido.

## Créditos

Este proyecto fue creado por Franco Sebastián Torres Vidal.

## Licencia

Este proyecto está bajo la licencia MIT.
