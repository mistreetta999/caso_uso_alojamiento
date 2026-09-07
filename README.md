<<<<<<< HEAD

## 🏢 1. Estructura de la Base de Datos (Modelos)
Lo primero es definir qué datos vas a guardar. En tu archivo models.py necesitarás al menos tres tablas principales:

* Alojamiento: Para guardar el título, descripción, precio por noche, capacidad de huéspedes y fotos.
* Usuario/Cliente: Django ya incluye un sistema de usuarios integrado (User) para gestionar quién alquila y quién es el dueño.
* Reserva: Para conectar un usuario con un alojamiento, guardando la fecha de entrada, fecha de salida y el estado del pago.

## 📐 2. Formularios Inteligentes (forms.py)
En lugar de escribir código HTML largo para cada formulario, utiliza ModelForm de Django.

* Django lee tu modelo de alojamiento o reserva.
* Genera automáticamente los campos HTML correspondientes.
* Valida de forma segura que los datos ingresados sean correctos (por ejemplo, que el precio sea un número positivo).

## 🎨 3. Diseño con Bootstrap y CSS
Para que tus formularios se vean profesionales y se adapten a teléfonos móviles:

* Estilo rápido: Utiliza la librería django-crispy-forms con el paquete de Bootstrap. Permite renderizar formularios elegantes escribiendo solo {{ form|crispy }} en tu plantilla.
* Componentes útiles: Usa las Cards (tarjetas) de Bootstrap para mostrar la lista de alojamientos disponibles, y un Navbar (barra de navegación) para moverse por el sitio.

## 🚀 Pasos iniciales para arrancar hoy

   1. Crear el entorno virtual en tu terminal para aislar el proyecto.
   2. Instalar Django mediante pip install django.
   3. Iniciar el proyecto y la app con django-admin startproject y python manage.py startapp.




=======
# caso_uso_alojamiento
proyecto academico para examenes de alumna carolina mistretta 
>>>>>>> aaa5d9b14cc3630207f6eb52507004a8613ecd87
