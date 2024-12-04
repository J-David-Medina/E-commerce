# Proyecto Full Stack E-Commerce con Django, React y PostgreSQL

Este es un proyecto **e-commerce** de pila completa construido con **Django** para el backend, **React** con **TypeScript** para el frontend y **PostgreSQL** como base de datos. La plataforma permite a los usuarios ver y comprar productos. Los usuarios registrados pueden gestionar su perfil, ver su historial de compras y los vendedores pueden listar nuevos productos para la venta.

## Características

- **Listado de Productos**: Los usuarios pueden explorar y comprar productos.
- **Perfiles de Usuario**: Los usuarios registrados pueden crear cuentas, ver su historial de compras y gestionar su perfil.
- **Gestión de Productos**: Los vendedores pueden crear y gestionar productos en la tienda.
- **Autenticación**: Login y registro seguro para usuarios y vendedores.

## Tecnologías

- **Backend**: Django, Django REST Framework
- **Frontend**: React, TypeScript
- **Base de Datos**: PostgreSQL

## Instalación

### Backend

1. Clona el repositorio:

    ```bash
    git remote add origin https://github.com/J-David-Medina/E-commerce.git 
    cd Backend
    ```

2. Configura un entorno virtual:

    ```bash
    python -m venv venv
    source venv/bin/activate  # En Linux/Mac
    venv\Scripts\activate  # En Windows
    ```

3. Instala las dependencias:

    ```bash
    pip install -r requirements.txt
    ```

4. Configura PostgreSQL en `settings.py`.

5. Aplica las migraciones:

    ```bash
    python manage.py migrate
    ```

6. Inicia el servidor de desarrollo:

    ```bash
    python manage.py runserver
    ```

### Frontend

1. Navega al directorio del frontend:

    ```bash
    cd Frontend
    ```

2. Instala las dependencias:

    ```bash
    npm install 
    ```

3. Inicia el servidor de desarrollo de React:

    ```bash
    npm start 
    ```
