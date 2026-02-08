# Tenerife Grand Hotel - App de Gestión de Reservas

![Python](https://img.shields.io/badge/Python-3.10%2B-blue)
![Flet](https://img.shields.io/badge/Flet-Frontend-purple)
![MongoDB](https://img.shields.io/badge/MongoDB-Database-green)
![Poetry](https://img.shields.io/badge/Poetry-Dependency%20Manager-blue)
![Pytest](https://img.shields.io/badge/Pytest-Testing-yellow)

**Tenerife Grand Hotel** es una aplicación de escritorio multiplataforma desarrollada como Proyecto de Aprendizaje Basado en Proyectos (ABP). La aplicación permite la gestión integral de reservas hoteleras, ofreciendo una interfaz moderna e intuitiva construida con **Flet** (Python) y respaldada por una base de datos documental en **MongoDB**.

---

## Tabla de Contenidos

1. [Descripción y Contexto](#-descripción-y-contexto)
2. [Características Principales](#-características-principales)
3. [Tecnologías Utilizadas](#-tecnologías-utilizadas)
4. [Estructura del Proyecto](#-estructura-del-proyecto)
5. [Instalación y Despliegue](#-instalación-y-despliegue)
6. [Testing](#-testing)
7. [Autores](#-autores)

---

## Descripción y Contexto

El objetivo principal de este proyecto es diseñar y desarrollar una aplicación funcional que resuelva la necesidad práctica de gestionar reservas en un hotel. La aplicación implementa un sistema **CRUD** (Crear, Leer, Actualizar, Eliminar) completo, permitiendo a los usuarios interactuar con la base de datos de manera eficiente y segura.

La solución se centra en la experiencia del usuario (UX), ofreciendo navegación fluida, validación de datos y feedback visual inmediato ante las acciones del usuario.

---

## Características Principales

### Gestión de Usuarios
* **Registro e Inicio de Sesión:** Sistema de autenticación seguro para acceder a las funcionalidades de reserva.
* **Perfil de Usuario:** Visualización y edición de datos personales (Nombre, Teléfono, Contraseña).
* **Eliminación de Cuenta:** Funcionalidad para borrar la cuenta de forma permanente con confirmación de seguridad.

### Gestión de Habitaciones y Catálogo
* **Exploración Visual:** Carrusel de imágenes y tarjetas detalladas de las habitaciones (Presidential, Luxury, Apartment, etc.).
* **Filtros Avanzados:** Búsqueda en tiempo real por fechas, huéspedes, precio, servicios y categoría.

### Sistema de Reservas (Core)
* **Disponibilidad en Tiempo Real:** Verificación de fechas para evitar solapamientos de reservas.
* **Proceso de Pago Simulado:** Cálculo automático de precios (Noches + IVA) y formulario de datos de facturación.
* **Mis Reservas:** Panel para visualizar historial, modificar fechas o cancelar estancias.

### Reseñas y Calidad
* **Valoraciones:** Sistema de estrellas y comentarios.
* **Alta Fiabilidad:** Código testeado con Pytest para asegurar la robustez de las funciones críticas.

---

## Tecnologías Utilizadas

* **Lenguaje:** Python 3.10+
* **Frontend:** [Flet](https://flet.dev) (Framework UI).
* **Backend:** MongoDB (NoSQL) con Pymongo.
* **Testing:** [Pytest](https://docs.pytest.org/) (Pruebas unitarias).
* **Gestión de Dependencias:** Poetry.
* **Control de Versiones:** Git & GitHub.

---

## Estructura del Proyecto

El código sigue una **arquitectura modular** estricta. Se ha incluido un directorio de pruebas dentro de `src` para validar la lógica de negocio.

```text
TenerifeGrandHotel/
├── assets/                 # Imágenes, iconos y recursos estáticos
│   ├── media/
├── src/
│   ├── Backend/            # Lógica de Negocio y Acceso a Datos
│   │   ├── BookingManagement.py
│   │   ├── RoomsManagement.py
│   │   ├── UsersManagement.py
│   │   └── Utils/          # Validaciones y configuración
│   ├── components/         # Componentes UI reutilizables (Navbar, Cards)
│   ├── test/               # Batería de Pruebas (Pytest) [NUEVO]
│   │   ├── test_bookings.py
│   │   ├── test_users.py
│   │   └── ...
│   └── views/              # Pantallas de la aplicación (Flet Views)
│       ├── home_page.py
│       ├── user_page.py
│       ├── booking_process.py
│       └── ...
├── app.py                  # Punto de entrada (Main)
├── pyproject.toml          # Configuración de dependencias (Poetry)
└── README.md               # Documentación
