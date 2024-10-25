# Aguilar Entrega

## Descripción
Aguilar Entrega es un proyecto desarrollado en Django que permite gestionar un sistema de usuarios, donde se pueden registrar, iniciar sesión y editar su perfil. El objetivo del proyecto es ofrecer una plataforma fácil de usar para la gestión de usuarios y sus datos.

## Características
- Registro de usuarios
- Inicio de sesión
- Edición de perfil
- Visualización de información de usuario
- Gestión de permisos de staff y clientes

## Tecnologías Utilizadas
- [Django](https://www.djangoproject.com/) - Framework web para desarrollo en Python
- [Bootstrap](https://getbootstrap.com/) - Framework CSS para diseño responsivo
- [HTML/CSS](https://developer.mozilla.org/en-US/docs/Web/HTML) - Lenguajes de marcado y estilo

## Instalación

1. Clona el repositorio:
  git clone https://github.com/LautaroAguila/Aguilar-Entrega.git
2. Navega al directorio del proyecto:
  cd Aguilar-Entrega
3. Crea un entorno virtual:
  python -m venv venv
4. Activa el entorno virtual:
  - En Windows:
      venv\Scripts\activate
  - En macOS/Linux:
      source venv/bin/activate
5. Instala las dependencias:
  pip install -r requirements.txt
6. Ejecuta las migraciones de la base de datos:
  python manage.py migrate
7. Inicia el servidor:
  python manage.py runserver
8. Accede a la aplicación en tu navegador:
  http://127.0.0.1:8000/

## Uso
Una vez que la aplicación esté en funcionamiento, podrás registrarte como nuevo usuario o iniciar sesión si ya tienes una cuenta. Podrás acceder a tu perfil, ver tu información y editarla según sea necesario. Ademas si eres un usario con permisos, ya sea superuser o staff, podras editar, crear o eliminar productos, segun corresponda.
