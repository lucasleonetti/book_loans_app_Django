# Django App para la gestión de prestamos de libros a clientes

## Descripción del proyecto

Este proyecto es una aplicación web desarrollada en Django que permite la gestión de un sistema de prestamos de libros a clientes. La aplicación permite registrar clientes, libros y prestamos. Asi como tambien la visualizacion de los prestamos activos y la devolucion de los libros prestados.

Gestión de clientes:

- Crear, editar y eliminar clientes.
- Visualizar la lista de clientes registrados.

Gestión de libros:

- Crear, editar y eliminar libros.
- Visualizar la lista de libros registrados.

Gestión de prestamos:

- Crear prestamos.
- Visualizar la lista de prestamos activos.
- Devolver libros prestados.

## Instrucciones para la ejecucion del proyecto

- Clonar el repositorio

```bash
git clone 
```

- Instalar las dependencias

```bash
pip install -r requirements.txt
```

- Lanzar el servidor

```bash
python manage.py runserver
```

- Acceder a la aplicación en el navegador

```bash
http://localhost:8000/book_loans/
```

### Importante

Si por algun motivo ocurre algun error o no puede visualizar los datos ya cargados en la base de datos, intente con ejecutar las migraciones nuevamente.

```bash
python manage.py migrate
```

## Casos de prueba

En el archivo 'casos_de_prueba.xlsx' se encuentran los casos de prueba realizados para la aplicación.
