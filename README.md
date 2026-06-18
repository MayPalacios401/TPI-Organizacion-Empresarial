# TPI - Organización Empresarial

## Integrantes

* Mayra Palacios
* Ammiel Vainstein

## Comisión

15

## Materia

Organización Empresarial

## Profesor

Mario López

## Tutor

Pablo García

## Carrera

Tecnicatura Universitaria en Programación a Distancia (UTN)

---

# Tema del Proyecto

**Automatización del proceso de gestión de vacaciones mediante un chatbot.**

---

# Descripción

El presente trabajo tiene como objetivo analizar y optimizar el proceso de solicitud de vacaciones dentro de una organización.

Actualmente, este procedimiento se realiza de forma manual mediante correos electrónicos y validaciones efectuadas por el área de Recursos Humanos, lo que genera demoras, errores de registro y una experiencia poco eficiente para los empleados.

Como propuesta de mejora, se plantea la implementación de un chatbot capaz de gestionar solicitudes de vacaciones de manera automática, validando la existencia del empleado, consultando el saldo disponible de días y aprobando o rechazando solicitudes según las reglas de negocio definidas.

El proyecto integra conceptos de modelado de procesos mediante BPMN 2.0, gestión de estados, validación de datos, simulación de persistencia y automatización de procesos administrativos.

---

# Objetivos

* Analizar un proceso administrativo existente.
* Modelar el proceso actual (AS-IS).
* Diseñar un proceso optimizado (TO-BE).
* Simular un chatbot capaz de ejecutar el proceso.
* Implementar una máquina de estados para controlar el flujo de interacción.
* Aplicar validaciones y manejo de errores.
* Utilizar GitHub como herramienta de gestión y control de versiones.

---

# Tecnologías y Herramientas Utilizadas

* Python
* CSV (Base de datos simulada)
* GitHub
* BPMN 2.0
* Draw.io / Bizagi Modeler
* ChatGPT
* Claude

---

# Funcionalidades del Chatbot

* Solicitar número de legajo.
* Verificar existencia del empleado.
* Consultar saldo disponible de vacaciones.
* Solicitar cantidad de días requeridos.
* Aprobar o rechazar solicitudes.
* Actualizar el saldo disponible.
* Gestionar errores de entrada.
* Mantener el contexto mediante una máquina de estados.

---

# Estructura del Repositorio

```text
TPI-Organizacion-Empresarial
│
├── README.md
│
├── chatbot
│   └── chatbot_vacaciones.py
│
├── base_datos
│   ├── empleados.csv
│   └── Base de datos original.xlsx
│
├── documentacion
│   └── TPI_Organizacion_Empresarial.pdf
│
└── capturas
    ├── BPMN_AS_IS.png
    ├── BPMN_TO_BE.png
    ├── consultas_IA.png
    └── repositorio_github.png
```

---

# Ejecución del Proyecto

1. Descargar o clonar el repositorio.
2. Verificar que el archivo `empleados.csv` se encuentre dentro de la carpeta `base_datos`.
3. Ejecutar el archivo:

```bash
python chatbot_vacaciones.py
```

4. Ingresar el número de legajo solicitado por el sistema.
5. Seguir las instrucciones mostradas por el chatbot.

---

# Base de Datos Simulada

El sistema utiliza un archivo CSV denominado `empleados.csv` para almacenar la información de los empleados y sus días de vacaciones disponibles.

### Campos principales

* Legajo
* Nombre
* Días disponibles
* Estado

---

# BPMN

El proyecto incluye:

* Diagrama BPMN AS-IS (proceso actual).
* Diagrama BPMN TO-BE (proceso automatizado).

Ambos modelos representan las actividades del usuario, las acciones del sistema y los puntos de decisión necesarios para la gestión de vacaciones.

---

# Gestión de Estados

El chatbot implementa una máquina de estados que permite identificar en qué etapa del proceso se encuentra cada usuario.

### Estados principales

* Inicio
* Esperando Legajo
* Validando Empleado
* Mostrando Saldo
* Esperando Solicitud
* Evaluando Solicitud
* Solicitud Aprobada
* Solicitud Rechazada
* Fin

---

# Robustez

El sistema contempla distintos escenarios de error:

* Legajo inexistente.
* Texto en lugar de valores numéricos.
* Solicitud de más días que los disponibles.
* Cantidades negativas o inválidas.
* Saldo disponible igual a cero.

---

# Uso de Inteligencia Artificial

Durante el desarrollo del proyecto se utilizaron ChatGPT y Claude como herramientas de apoyo para:

* Diseño inicial del proceso.
* Identificación de caminos felices e infelices.
* Revisión de la coherencia entre BPMN, máquina de estados y código.
* Generación de ejemplos de pruebas.
* Revisión de documentación.

Todas las respuestas obtenidas fueron analizadas, adaptadas y validadas por los integrantes antes de ser incorporadas al trabajo final.

---

# Repositorio Académico

Trabajo Práctico Integrador desarrollado para la materia Organización Empresarial de la Tecnicatura Universitaria en Programación a Distancia (UTN).

**Año: 2026**

