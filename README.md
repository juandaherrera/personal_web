# 👋🏻 Bienvenido a mi Web

[![Python](https://img.shields.io/badge/Python-3.11+-yellow?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://python.org)
[![Reflex](https://img.shields.io/badge/Reflex-0.4.1-5646ED?style=for-the-badge&logo=python&logoColor=white&labelColor=101010)](https://reflex.dev)

## Descripción
Este es mi rincón digital, un espacio donde convergen mi vida profesional y, próximamente, también la personal. Como profesional apasionado por los datos, esta web es el reflejo de mi carrera: mis proyectos, estudios, logros y aspectos personales que definen mi trayectoria. Aquí encontrarás una mezcla de experiencias y conocimientos que he ido acumulando a lo largo de mi vida profesional.

## Características
El sitio está estructurado en cinco secciones principales que representan diferentes aspectos de mi perfil:

* **Mi presentación:** una breve introducción a quién soy y lo que hago.
* **Acerca de mí:** un vistazo más personal a mis intereses y pasiones.
* **Experiencia:** Un recorrido por mi trayectoria profesional.
* **Proyectos:** Una vitrina de los proyectos que he desarrollado.
* **Educación:** Mis credenciales académicas y formación profesional.

### Próximas Características 
![Work in Progress](https://img.shields.io/badge/status-work_in_progress-yellow)

* [X] Sección de Cursos.
* [X] Sección de Certificaciones.
* [ ] Testimonios / Recomendaciones.
* [ ] Formulario de contacto.
* [ ] Switch de idioma [ES / EN]


## Instalación y despliegue local

### Para visualizar el sitio web con Docker:

1. Clona el repositorio:
   ```bash
   git clone https://github.com/juandaherrera/personal_web.git
   ```
2. Navega al directorio del proyecto:
   ```bash
   cd personal_web
   ```
3. Crea una imagen del [Dockerfile](Dockerfile):
   ```bash
   docker build -t reflex-project:latest .
   ```
4. Corre un contenedor con la imagen creada:
   ```bash
   docker run -d -p 80:80 --name personal_web reflex-project:latest
   ```

Nota: actualmente el proyecto solo tiene desplegado el frontend en [Railway](https://railway.app/). Es por esa razón que se corre en un servidor [NGINX](https://www.nginx.com/) desde el [Dockerfile](Dockerfile).

## Contacto
Si tienes preguntas, sugerencias o simplemente quieres conectarte, no dudes en contactarme a través de:
| Red | Contacto |
| --- | -------- |
| Correo | juandaherreparra@gmail.com | 
| LinkedIn | [![Linkedin: Juan David Herrera](https://img.shields.io/badge/-JuanDavidHerrera-blue?style=flat-square&logo=Linkedin&logoColor=white&link=https://www.linkedin.com/in/juan-david-herrera/)](https://www.linkedin.com/in/juan-david-herrera/) |

