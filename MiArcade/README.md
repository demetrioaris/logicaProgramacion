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

- **Enfoque Algorítmico:**
  - **Validación de entrada defensiva:** Uso de bucles `while` con `try-except` para garantizar que la cantidad de rondas ingresada sea un entero positivo mayor que cero, y que la jugada pertenezca estrictamente al universo de opciones válidas.
  - **Aleatoriedad estocástica:** Selección no predecible de la máquina mediante `random.choice()`.
  - **Evaluación lógica:** Matriz de condiciones booleanas compuestas para resolver victorias, derrotas y empates.
  - **Seguimiento de historial:** Almacenamiento continuo en listas y análisis de resultados finales empleando `list.count()` y numeración con `enumerate()`.

---

### 2. Cazafantasmas 2.0: Escudo Ectoplásmico

> 💼 **Caso de Negocio / Simulación Profesional:**  
> Este proyecto fue concebido y desarrollado bajo la simulación de un encargo corporativo real: una entidad educativa contrata a un equipo de desarrollo de software para construir un videojuego interactivo de entrenamiento matemático para estudiantes de educación primaria.

- **Requerimientos Pedagógicos y de Negocio Resueltos:**
  - **Matemáticas adaptadas a primaria:** Generación dinámica de desafíos aritméticos (suma, resta, multiplicación y división). El algoritmo garantiza que las restas nunca generen números negativos (`n2 <= n1`) y que las divisiones sean siempre exactas sin decimales (`n1 = n2 * solucion`), asegurando una experiencia didáctica estimulante y pedagógicamente correcta.
  - **Economía de juego (Diccionarios):** Catálogo de artefactos estructurado mediante diccionarios (`dict`), asociando cada herramienta (`red`, `aspiradora`, `laser`) a un puntaje específico de recompensa. Se captura de forma controlada el error `KeyError` si el usuario intenta equipar un artículo inexistente.
  - **Protocolo de Tolerancia a Fallos Completo (`try - except - else - finally`):**
    - `try`: Captura la respuesta numérica del usuario protegiendo la ejecución de posibles caídas.
    - `except ValueError`: **Escudo protector:** Si el niño introduce accidentalmente letras, espacios o caracteres especiales, el sistema no colapsa; activa un escudo ectoplásmico seguro notificando el evento.
    - `else`: Ejecución de lógica de recompensa y validación de respuesta únicamente cuando la conversión a entero fue exitosa.
    - `finally`: Rutina obligatoria del sistema; disminuye la batería y enfría el equipo tras cada ronda de forma incondicional, simulando la telemetría del artefacto.

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
