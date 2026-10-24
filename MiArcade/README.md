# 🕹️ MiArcade - Virtual Game Hub

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Cisco Networking Academy](https://img.shields.io/badge/Cisco_Networking_Academy-Course_Project-049fd9?style=for-the-badge&logo=cisco&logoColor=white)](https://www.netacad.com/)
[![FUNDESTEAM](https://img.shields.io/badge/FUNDESTEAM-Panamá-FF6F00?style=for-the-badge)](https://fundesteam.org/)
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)]()

> **MiArcade** es un centro de videojuegos clásicos e interactivos desarrollados en consola con Python. El proyecto está diseñado con un enfoque de ingeniería de software profesional, orientado a demostrar dominio en **lógica algorítmica, programación estructurada, modularización, manejo robusto de excepciones y experiencia de usuario (UX) en terminal**.

---

## 📌 Contexto Institucional

Este proyecto fue desarrollado y estructurado en el marco del programa formativo **"Fundamentos de Python 1"**, impulsado en colaboración por **Cisco Networking Academy** y **FUNDESTEAM Panamá**. Representa la consolidación práctica de competencias técnicas esenciales para el desarrollo de software y la resolución sistemática de problemas algorítmicos.

---

## 🎯 Competencias Técnicas Adquiridas

El desarrollo de este ecosistema de juegos abarca cuatro bloques curriculares progresivos:

- **Bloque 1: Principios Fundamentales del Lenguaje**
  - Sintaxis estricta, semántica y comprensión del modelo de ejecución de Python.
  - Reglas de indentación, flujo lógico secuencial, literales, variables y operaciones fundamentales de entrada y salida (`input()`, `print()`).
  - Interpretación, depuración y corrección proactiva de mensajes de error de sintaxis y tiempo de ejecución.

- **Bloque 2: Tipos de Datos y Operaciones Aritmético-Lógicas**
  - Manipulación precisa de tipos de datos primitivos (`int`, `float`, `str`, `bool`) y conversión de tipos (_type casting_).
  - Álgebra booleana, precedencia de operadores lógicos y aritméticos.
  - Procesamiento y saneamiento de cadenas de texto (`.strip()`, `.lower()`, `.upper()`).

- **Bloque 3: Estructuras de Flujo de Control**
  - Bifurcación condicional avanzada y exhaustiva (`if`, `elif`, `else`).
  - Estructuras de control iterativas (`for`, `while`) para bucles infinitos controlados y recorridos secuenciales.
  - Control fino de ciclos mediante directivas de interrupción (`break`) y continuación condicional (`continue`).

- **Bloque 4: Colecciones, Modularización y Robustez**
  - Estructuras de datos complejas: listas dinámicas, tuplas, diccionarios asociativos y conjuntos (`set`).
  - Modularización con funciones de usuario (`def`), desacoplamiento, paso de parámetros, valor de retorno y ámbito léxico (_scope_).
  - Integración de módulos nativos de la biblioteca estándar de Python: `random`, `string`, `os`.
  - Gestión profesional y resiliente de excepciones mediante la suite completa `try`, `except`, `else` y `finally`.

---

## 📁 Arquitectura del Proyecto

El proyecto sigue una arquitectura modular en paquetes independientes orquestados por un punto de entrada central:

```text
MiArcade/
│
├── menu_principal.py               # Orquestador principal y hub del Arcade
│
├── config/                         # Paquete transversal: configuraciones y utilidades (DRY)
│   ├── __init__.py
│   └── utils.py                    # Limpieza de terminal y confirmación interactiva
│
├── piedra_papel_y_tijera/          # Módulo: Juego 1
│   ├── __init__.py
│   └── piedra_papel_y_tijera.py    # Lógica de rondas, torneos y estadísticas
│
├── cazafantasma/                   # Módulo: Juego 2 (Simulación de Caso de Negocio)
│   ├── __init__.py
│   └── cazafantasmas.py            # Motor matemático adaptativo con suite try/except/else/finally
│
└── ahorcado/                       # Módulo: Juego 3
    ├── __init__.py
    ├── ahorcado.py                 # Lógica de juego, sets de letras y renderizado dinámico
    ├── hangman_visual.py           # Diccionario de arte visual ASCII por niveles de vidas
    └── palabras.py                 # Banco léxico desacoplado
```

---

## 🎮 Catálogo de Juegos y Demostración Técnica

### 1. Piedra, Papel o Tijera

Un simulador de torneos por rondas contra la computadora con análisis estadístico en tiempo real.

- **Enfoque Algorítmico y de UX:**
  - **Experiencia de usuario ágil y mapeo asociativo:** Menú de opciones intuitivo que acepta tanto números (`1`, `2`, `3`) como palabras (`piedra`, `papel`, `tijera`) mediante diccionarios de mapeo (`dict`).
  - **Marcador en vivo y terminal limpia (Clean UX):** Refresco dinámico con `os.system` que mantiene el encabezado, la ronda actual y el marcador en vivo (`👤 Tú vs 🤖 CPU`) fijos en pantalla sin desplazamiento molesto.
  - **Validación defensiva con excepciones (`try - except ValueError`):** Control estricto de entradas que intercepta valores no permitidos mediante `raise ValueError`, garantizando tolerancia a fallos.
  - **Aleatoriedad estocástica y lógica de juego:** Selección de la máquina con `random.choice()` y resolución booleana precisa de victorias, derrotas y empates.
  - **Historial de torneo y rejugabilidad:** Registro completo de rondas en tuplas, proclamación de campeón al cierre y ciclo interactivo para reiniciar torneos o volver al menú principal.

---

### 2. Cazafantasmas Matemático

> 💼 **Caso de Negocio / Simulación Profesional:**  
> Este proyecto fue concebido y desarrollado bajo la simulación de un encargo corporativo: una entidad educativa contrata a un equipo de desarrollo de software para construir un videojuego interactivo, ágil y gamificado de entrenamiento matemático para estudiantes de primaria que inician en aritmética.

- **Requerimientos Pedagógicos y de Gamificación Resueltos:**
  - **Interacción directa sin fricción (Zero Typing Overhead):** Diseñado específicamente para niños que aún no dominan la mecanografía. El juego va directo a la acción: el niño solo utiliza el teclado numérico para disparar la solución matemática, eliminando ingresos innecesarios de palabras.
  - **Aritmética adaptada a primaria:** Generador dinámico de operaciones básicas (suma, resta, multiplicación y división). El algoritmo asegura que las restas nunca arrojen resultados negativos (`n2 <= n1`) y que las divisiones sean siempre exactas sin decimales (`n1 = n2 * solucion`), fomentando el aprendizaje sin frustración.
  - **Gamificación visual:** Sistema de vidas con corazones (`❤️ ❤️ ❤️`), puntaje acumulativo por fantasmas cazados (`+10 puntos`) y avance progresivo de misiones por rondas.
  - **Tolerancia a fallos con escudo protector (`try - except ValueError - else`):** Si el niño presiona accidentalmente letras o símbolos, el sistema atrapa el `ValueError` y despliega un mensaje protector sin quitarle vidas ni perder el turno.
  - **Experiencia de usuario limpia (Clean UX):** Limpieza dinámica de terminal (`os.system`) para mantener el tablero fijo sin desplazamiento de pantalla y ciclo de revancha interactivo.

---

### 3. Ahorcado (Hangman)

Recreación del clásico juego de palabras con interfaz dinámica de consola y optimización en estructuras de datos.

- **Enfoque Algorítmico y de UX:**
  - **Validación Defensiva con Excepciones (`try - except ValueError`):** Empleo de `raise ValueError` para interceptar de inmediato entradas inválidas (más de una letra, números, caracteres especiales o letras ya usadas) y capturarlas con `except ValueError as error`, evitando penalizaciones de vidas por errores de formato.
  - **Álgebra de Conjuntos (`set`):** Manejo eficiente de colecciones no repetidas. Se utiliza la diferencia de conjuntos (`abecedario - letras_usadas`) para comprobar letras válidas restantes en tiempo $O(1)$.
  - **Comprensión de Listas (_List Comprehensions_):** Renderizado dinámico de la palabra oculta reemplazando letras no descubiertas por guiones de forma declarativa y legible.
  - **Arquitectura de Datos Desacoplada:** El catálogo de palabras y las representaciones visuales en arte ASCII del muñeco se distribuyen en módulos separados (`palabras.py` y `hangman_visual.py`), respetando el principio de responsabilidad única.
  - **Experiencia de Usuario en Terminal (Clean UX):** Integración con el sistema operativo (`os.system`) para limpiar la pantalla en cada jugada (`cls` en Windows / `clear` en Unix), evitando el desplazamiento excesivo (_scroll_) y conservando el dibujo y estado visual en una posición fija.
  - **Control de Rejugabilidad:** Ciclo de confirmación final que permite reiniciar el juego con una palabra nueva o retornar limpiamente al menú central.

---

### 4. Menú Principal (Hub Central)

Orquestador que centraliza el acceso a todos los juegos.

- **Patrón Modular:** Aplica la convención estándar `from [paquete] import [módulo]` y la invocación uniforme de la interfaz pública `.jugar()`.
- **Guardia de Ejecución (`if __name__ == '__main__':`):** Garantiza que cada juego pueda ser ejecutado tanto de manera individual e independiente como a través del menú unificado sin ejecuciones colaterales involuntarias.

---

## 🚀 Instalación y Ejecución

### Prerrequisitos

- Tener instalado **Python 3.8** o superior en el sistema. Puedes comprobarlo ejecutando:
  ```bash
  python --version
  ```

### Ejecución

1. Clona este repositorio o descarga la carpeta del proyecto:

   ```bash
   git clone https://github.com/tu-usuario/MiArcade.git
   cd MiArcade
   ```

2. Ejecuta el centro de juegos desde la terminal:

   ```bash
   python menu_principal.py
   ```

3. _(Opcional)_ Si deseas probar cualquiera de los juegos de manera independiente:
   ```bash
   python -m piedra_papel_y_tijera.piedra_papel_y_tijera
   python -m cazafantasma.cazafantasmas
   python -m ahorcado.ahorcado
   ```

---

## 👨‍💻 Créditos y Reconocimientos

- **Desarrollador / Autor:** Estudiante de Lógica de Programación y Desarrollo de Software.
- **Curso:** _Fundamentos de Python 1_.
- **Instituciones Aliadas:** **Cisco Networking Academy** & **FUNDESTEAM Panamá**.
