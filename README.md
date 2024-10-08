# Talana Kombat

Descripción
Talana Kombat es un juego basado en texto donde dos personajes, Tonyn Stallone y Arnaldor Shuatseneguer, se enfrentan en un combate hasta la muerte. Cada personaje tiene una serie de movimientos especiales y ataques básicos que se ejecutan en turnos, similar a un juego de rol japonés (JRPG).

Este proyecto incluye la implementación del juego en Python y las pruebas unitarias para verificar el correcto funcionamiento de la lógica del juego. Todo el entorno se puede ejecutar dentro de un contenedor Docker para garantizar la portabilidad y consistencia.

## Requisitos:

    1) Docker instalado en tu máquina
    
    2) Python 3.9 (si deseas ejecutar el código localmente)

## Estructura del Proyecto:

    1) Dockerfile
    
    2) README.md
    
    3) talana_kombat.py
    
    4) test_talana_kombat.py

Dockerfile: Archivo de configuración para construir la imagen Docker.
README.md: Archivo de documentación.
talana_kombat.py: Implementación principal del juego.
test_talana_kombat.py: Pruebas unitarias utilizando unittest.

## Uso.

### 1. Clona el repositorio:

Copiar código bash:

    git clone https://github.com/cristianhinojosa/TalanaKombat
    
    cd TalanaKombat


### 2. Construye la imagen Docker

Copiar código bash:

    docker build -t talana_kombat .

### 3. Ejecuta el contenedor en Docker

Copiar código bash:
    
    docker run --rm talana_kombat
   
Este comando mostrará los resultados en la terminal.

### 4. Ejecuta el juego localmente (opcional)

Si prefieres ejecutar el juego fuera de Docker, puedes hacerlo directamente con Python:


Copiar código bash:

    python talana_kombat.py


### 5. Ejemplos de Combate

Para ver ejemplos de cómo se desarrollan los combates, revisa los casos de prueba en test_talana_kombat.py.


### Realizado por Cristian Hinojosa el 8/8/2024
