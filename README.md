# 📂 Sistema de Portafolios Profesionales

Un sistema web desarrollado en **Django** que permite a los usuarios crear, gestionar y mostrar su portafolio profesional de manera sencilla y rápida. Cada usuario puede registrar su información personal, proyectos, tecnologías utilizadas y una breve descripción de su perfil, fomentando así la visibilidad y difusión de talentos tanto en el área de desarrollo como en otras disciplinas.

---

## 🚀 Características

- **Gestión de usuarios**: creación, inicio y cierre de sesión con validaciones y mensajes de alerta.
- **Perfil personal**: nombre, apellido, descripción y foto de perfil.
- **Gestión de proyectos**: cada usuario puede registrar múltiples proyectos con descripción, tecnologías y enlaces.
- **Relación uno a muchos**: un usuario puede tener varios proyectos asociados.
- **Interfaz amigable**: plantillas HTML integradas con **Bootstrap** para una experiencia limpia y responsiva.
- **Mensajes dinámicos**: alertas de éxito, error y advertencia con `django.contrib.messages`.

---

## 🛠️ Tecnologías utilizadas

- [Python 3](https://www.python.org/)  
- [Django](https://www.djangoproject.com/)  
- [SQLite](https://www.sqlite.org/) (por defecto, aunque puede migrarse a otra base de datos)  
- [HTML5 & CSS3](https://developer.mozilla.org/es/docs/Web)  

---

## 📌 Requisitos previos

Antes de iniciar, asegúrate de tener instalado:

- Python 3.10 o superior  
- pip (gestor de paquetes de Python)  
- Virtualenv (opcional, recomendado)  

---

## ⚙️ Instalación

1. Clonar el repositorio:
   '''bash
   git clone https://github.com/MiguelG2000/Magnifolio.git
   cd portafolios
   
3. Crear y activar un entorno virtual:
   python -m venv venv
   source venv/bin/activate   # En Linux/Mac
   venv\Scripts\activate      # En Windows
   
5. Instalar dependencias:
   pip install -r requirements.txt
   
7. Aplicar migraciones:
   python manage.py migrate
   
9. Crear un superusuario (administrador):
   python manage.py createsuperuser
   
11. Ejecutar el servidor de desarrollo:
   python manage.py runserver
   
---

👨‍💻 Autor

Miguel Angel Gonzalez Rodriguez
Desarrollador Backend con experiencia en Django, bases de datos y sistemas CRUD.
