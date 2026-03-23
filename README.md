[![Review Assignment Due Date](https://classroom.github.com/assets/deadline-readme-button-22041afd0340ce965d47ae6ef1cefeee28c7c493a6346c4f15d667ab976d596c.svg)](https://classroom.github.com/a/09uckVan)

# Recetario y Gestor de Menús
[//]: # (Incluid aquí la descripción de vuestra aplicación. Por cierto, así se ponen comentarios en Markdown)
La aplicación permite gestionar un recetario de platos e ingredientes. Permite crear ingredientes de distintos tipos (animal, vegetal, mineral), combinarlos en platos (veganos o con carne) y organizar el recetario de forma modular. Además, el sistema permite generar menús semanales, gestionar listas de la compra y exportar información en distintos formatos. Próximamente contará con una API REST para interactuar con los datos de manera externa.

## Autores

* (Coordinador) [Alfonso Íñiguez Cortés](https://github.com/Alfonso647)
* [Miguel Pérez Alonso](https://github.com/mpa113)

## Profesor
[//]: # (Indicar el profesor de la asignatura)
Cristina Cachero

## Requisitos
[//]: # (Indicad aquí los requisitos de vuestra aplicación, así como el alumno responsable de cada uno de ellos)
* Python 3.10 o superior 
* pip para instalar dependencias 
* Entorno virtual recomendado 

## Instrucciones de instalación y ejecución
[//]: # (instrucciones de ejecución)
Para ejecutar nuestra aplicación hay que instalar las dependencias desde el requirements.txt. Seguidamente ejecuta el main para probar la aplicación.

1. Clonar el repositorio:
```bash
git clone https://github.com/trabajo-final-a8.git
cd trabajo-final-a8
```

2. Crear un entorno virtual (opcional, pero recomendado):
```bash
python -m venv venv
# Activar en Windows
venv\Scripts\activate
# Activar en Linux/macOS
# source venv/bin/activate
```

3. Instalar dependencias:
```bash
pip install -r requirements.txt
```

4. Ejecutar la aplicación:
```bash
python main.py
```

## Resumen de la API
[//]: # (documentación acerca de la API)
La API REST estará disponible próximamente y permitirá:

* Crear, listar, actualizar y eliminar ingredientes
* Crear, listar y modificar platos
* Asociar ingredientes a platos
* Consultar recetas y detalles de los ingredientes

## Menú de aplicación

[//]: # (para la evaluación por pares, indicaréis aquí las diferentes opciones de vuestro menú textual, especificando para qué sirve cada una de ellas)

La aplicación contará con un menú interactivo que permitirá:

* Añadir ingredientes de distintos tipos (Animal, Vegetal, Mineral)
* Crear platos veganos o con carne
* Listar todos los platos y todos los ingredientes
* Consultar información detallada de cada receta
* Gestionar recetario
* Generar menú semanal
* Guardar y cargar menús
* Exportar menú a formato PDF