# 📇 Agenda de Contactos - Sistema Web CRUD con Django y MariaDB

Mini proyecto integrador desarrollado para la asignatura **Electiva Profesional III – Frameworks** (Ingeniería de Sistemas).

Este sistema web permite gestionar una agenda completa de contactos (personales, laborales, académicos e institucionales), aplicando los fundamentos del framework **Django** mediante su ORM, vistas, formularios, URLs y plantillas HTML integradas con **MariaDB**.

---

## 🚀 Características Principales

* **C (Create):** Formulario para la creación de nuevos contactos con validaciones y protección CSRF.
* **R (Read):** 
  * Listado general de contactos con contador en tiempo real.
  * Buscador interactivo por nombre, correo, ciudad o empresa.
  * Filtro desplegable por tipo de contacto (*Personal*, *Laboral*, *Académico*, *Institucional*).
  * Ficha de consulta detallada para visualizar toda la información individual de un contacto.
* **U (Update):** Formulario de edición precargado para modificar la información de registros existentes.
* **D (Delete):** Eliminación de contactos con pantalla de confirmación previa para evitar pérdidas accidentales.
* **Diseño Responsivo:** Interfaz moderna y adaptable construida con **Bootstrap 5** y **Bootstrap Icons**.

---

## 🛠️ Tecnologías Utilizadas

* **Lenguaje:** Python 3.14+
* **Framework Web:** Django 6.1
* **Base de Datos:** MariaDB / MySQL (vía `mysqlclient`)
* **Frontend:** HTML5, CSS3, Bootstrap 5, Bootstrap Icons

---

## 📋 Requisitos Previos

1. **Python 3.10+** instalado.
2. Servidor de base de datos **MariaDB** o **MySQL** activo en `localhost:3306`.
3. Paquetes de Python necesarios (`Django` y `mysqlclient`).

---

## ⚙️ Pasos para Ejecutar el Proyecto

### 1. Clonar el repositorio
```bash
git clone https://github.com/HaroldM126/Electiva_P3_Agenda_de_contactos-.git
cd Electiva_P3_Agenda_de_contactos-
```

### 2. Instalar dependencias (si aplica)
```bash
pip install django mysqlclient
```

### 3. Crear la Base de Datos en MariaDB
Asegúrate de que tu motor MariaDB/MySQL esté en ejecución y crea la base de datos:
```sql
CREATE DATABASE agenda_contactos_db CHARACTER SET utf8mb4 COLLATE utf8mb4_unicode_ci;
```

### 4. Configurar la conexión (Opcional)
Si tus credenciales de MariaDB son distintas a `USER='root'` y `PASSWORD='root'`, ajústalas en el archivo `agenda_project/settings.py`:
```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'agenda_contactos_db',
        'USER': 'root',
        'PASSWORD': 'tu_contraseña',
        'HOST': '127.0.0.1',
        'PORT': '3306',
    }
}
```

### 5. Ejecutar las migraciones
Aplica las migraciones para crear la estructura de tablas en MariaDB:
```bash
python manage.py makemigrations
python manage.py migrate
```

### 6. Iniciar el servidor de desarrollo
```bash
python manage.py runserver
```

### 7. Acceder a la aplicación
Abre tu navegador e ingresa a:
👉 [http://127.0.0.1:8000/](http://127.0.0.1:8000/)

---

## 📂 Estructura del Proyecto

```text
frameworks_taller_2/
├── agenda_project/         # Configuración global de Django (settings.py, urls.py)
├── contactos/              # Aplicación principal del módulo de agenda
│   ├── migrations/         # Migraciones de la base de datos
│   ├── templates/          # Plantillas HTML (base, lista, detalle, formulario, eliminar)
│   ├── admin.py            # Registro de modelos en el panel de administración
│   ├── forms.py            # Formulario ModelForm estilizado con Bootstrap
│   ├── models.py           # Modelo principal de la entidad Contacto
│   ├── urls.py             # Enrutamiento de URLs del CRUD
│   └── views.py            # Lógica de las vistas CRUD (Crear, Listar, Editar, Eliminar)
├── manage.py               # Script de administración de Django
└── README.md               # Documentación del proyecto
```

---

## 👨‍💻 Autor
Proyecto elaborado para el taller evaluativo de **Electiva Profesional III – Frameworks**.
