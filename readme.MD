# Deforestación y destrucción de habitats

## Descripción

En esta crud se encuentran las diferentes entidades que se van a crear en la base de datos con sus respectivos campos para diligenciar la gestión de los datos. En este caso, se va a utilizar el panel de Django para crear los diferentes modelos que se utilizarán en el proyecto.

## Instalación del proyecto

Para poder utilizar el proyecto, es necesario tener instalado en su computadora el entorno virtual de Python y el entorno de Django. Dependiendo del sistema operativo, pueden activar el entorno virtual de Python con el siguiente comando:

`python -m venv env`

Una vez activado el entorno virtual, se debe activar el entorno de Django con el siguiente comando:

`source env/bin/activate`

Luego, se debe instalar los requerimientos del proyecto con el siguiente comando:

`pip install -r requirements.txt`

Antes de poder utilizar el proyecto, se debe crear la base de datos con el siguiente comando, en MYSQL Workbench, si se utiliza el gestor de DB de  Xampp , saldrá un error, este comando debe ejecutarse en la terminal de MySQL Workbench:

`CREATE DATABASE deforestacion`

## Creación de la base de datos

Para crear la base de datos, se debe ejecutar el siguiente comando:

`python manage.py migrate`
`python manage.py makemigrations`
`python manage.py migrate`

Este comando creará la base de datos y los modelos correspondientes.

Ahora deberá crear un usuario administrador para poder acceder a la base de datos. Para ello, se debe ejecutar el siguiente comando:

`python manage.py createsuperuser`

Una vez ejecutado el comando, se debe ingresar el usuario y la contraseña para poder acceder a la base de datos.

Luego de tener las migraciones creadas y el usuario creado, se debe ejecutar el siguiente comando para correr el servidor de Django:

`python manage.py runserver`

Luego de eso, en el navegador, se debe acceder a la siguiente URL para acceder a la base de datos y debes iniciar la sesión con el usuario y contraseña que se creó anteriormente:

`http://localhost:8000/admin`

Y con esto, se debe poder acceder a la base de datos y crear los modelos correspondientes desde el panel de Django.

























