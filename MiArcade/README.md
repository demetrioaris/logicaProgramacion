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
├── menu_principal.py               # Orquestador principal y hub del Arcade (Pygame 60 FPS)
│
├── piedra_papel_y_tijera/          # Módulo: Juego 1
│   ├── __init__.py
│   └── piedra_papel_y_tijera.py    # Duelo clásico en Pygame con partículas y sonido
│
├── cazafantasma/                   # Módulo: Juego 2 (Simulación de Caso de Negocio)
│   ├── __init__.py
│   └── cazafantasmas.py            # Entrenador matemático interactivo en Pygame
│
├── ahorcado/                       # Módulo: Juego 3
│   ├── __init__.py
│   ├── ahorcado.py                 # Juego del ahorcado en Pygame con teclado virtual
│   └── palabras.py                 # Banco léxico desacoplado
│
└── serpiente/                      # Módulo: Juego 4 (Gráficos y Bucles de Eventos en Tiempo Real)
    ├── __init__.py
    └── juego_serpiente.py          # Motor Snake en Pygame a 60 FPS con cola de giros
```

---

## 🎮 Catálogo de Juegos y Demostración Técnica

### 1. Piedra, Papel o Tijera (Arcade 60 FPS con Pygame)

Videojuego visual en tiempo real a 60 FPS desarrollado con `pygame`, con gráficos vectoriales propios, animaciones físicas y síntesis de sonido.

- **Enfoque Algorítmico y de Videojuego 2D (`pygame`):**
  - **Gráficos Vectoriales Procedurales:** Renderizado de iconos para **Piedra**, **Papel** y **Tijera** usando primitivas geométricas (`pygame.draw.polygon`, `rect`, `circle`, `line`) sin depender de imágenes externas.
  - **Animación de Suspenso Sinusoidal:** Al elegir jugada, ambos emblemas oscilan con una onda sinusoidal (`math.sin`) antes de revelar el duelo.
  - **Sistema de Partículas y *Screen Shake*:** Explosión física de confeti con gravedad simulada al ganar y vibración de cámara (*screen shake*) al perder.
  - **Audio Retro Sintetizado (`array` + `pygame.mixer`):** Generación matemática de ondas sonoras de 8-bits en memoria para rebotes, victorias, derrotas y empates sin archivos `.wav` externos.
  - **Interacción Dual (Mouse + Teclado):** Botones con detección de colisión y efecto *hover* (`collidepoint`), además de atajos de teclado (`1`, `2`, `3`, `R`, `ESC`).

---

### 2. Cazafantasmas Matemático (Arcade 60 FPS con Pygame)

> 💼 **Caso de Negocio / Simulación Profesional:**  
> Este proyecto fue concebido y desarrollado bajo la simulación de un encargo corporativo: una entidad educativa contrata a un equipo de desarrollo de software para construir un videojuego interactivo, ágil y gamificado de entrenamiento matemático para estudiantes de primaria que inician en aritmética.

- **Requerimientos Pedagógicos y de Gamificación Resueltos (`pygame`):**
  - **Interacción Híbrida para Niños (Tarjetas Clicables + Teclado):** El niño puede resolver la operación haciendo clic directamente sobre una de las **4 tarjetas de respuesta en pantalla** o escribiendo el número en la caja de disparo y presionando `ENTER`.
  - **Fantasmas Animados Proceduralmente:** Fantasmas de distintos colores dibujados por código con movimiento de levitación sinusoidal (`math.sin`), falda ondulada y expresiones que reaccionan al impacto del rayo.
  - **Aritmética Adaptada a Primaria:** Generador dinámico de operaciones básicas (suma, resta, multiplicación y división). El algoritmo asegura que las restas nunca arrojen resultados negativos (`n2 <= n1`) y que las divisiones sean siempre exactas sin decimales (`n1 = n2 * solucion`).
  - **Rayo de Protones, Partículas y Audio 8-bits:** Disparo láser luminoso con explosión de partículas de ectoplasma al acertar, corazones vectoriales para las 3 vidas y efectos de sonido sintetizados en tiempo real.
  - **Tolerancia a Fallos con Escudo Protector (`try - except ValueError - else`):** Si el niño escribe letras o símbolos en la caja de texto, el sistema atrapa el `ValueError` y activa el escudo ectoplásmico sin quitarle vidas ni perder la ronda.

---

### 3. Ahorcado (Hangman - Arcade 60 FPS con Pygame)

Recreación gráfica del clásico juego de palabras con teclado virtual interactivo en pantalla, trazado vectorial progresivo y optimización en estructuras de datos.

- **Enfoque Algorítmico y de UX (`pygame`):**
  - **Teclado Virtual Interactivo + Teclado Físico:** Cuadrícula de 26 teclas (`A-Z`) en pantalla que cambian dinámicamente de color (verde si la letra está en la palabra, rojo oscuro si falló) con soporte simultáneo de teclado físico.
  - **Trazado Vectorial Progresivo (`dibujar_ahorcado`):** Dibujo paso a paso de la estructura y el personaje a lo largo de las 7 vidas usando primitivas geométricas, con partículas de confeti al ganar y *screen shake* al fallar.
  - **Validación Defensiva con Excepciones (`try - except ValueError`):** Empleo de `raise ValueError` para interceptar entradas inválidas o letras repetidas y capturarlas con `except ValueError as error`, evitando penalizaciones de vidas por errores de formato.
  - **Álgebra de Conjuntos (`set`) y Normalización Léxica:** Uso de conjuntos (`letras_palabra`, `letras_usadas`) para búsquedas en $O(1)$ y limpieza automática de tildes (`str.maketrans`) desde el módulo desacoplado `palabras.py`.
  - **Comprensión de Listas (_List Comprehensions_):** Renderizado dinámico de la palabra oculta revelando las letras acertadas en tiempo real.

---

### 4. La Serpiente (Snake Game - Arcade 60 FPS con Pygame)

Recreación gráfica en tiempo real del clásico arcade desarrollada con `pygame` a 60 FPS, con tablero ajedrezado, efectos de partículas, sonido 8-bits y personalización completa.

- **Enfoque Algorítmico y de Gráficos en Tiempo Real (`pygame`):**
  - **Tablero Matricial Ajedrezado (`28x22` celdas):** Cuadrícula visual con alternancia de tonos para facilitar la precisión espacial del jugador y marco neón dinámico según el tema elegido.
  - **Cola de Giros Anti-Input Lag:** Estructura de cola FIFO (`cola_direcciones`) que almacena hasta 2 giros anticipados a 60 FPS y previene giros suicidas de 180° inmediatos.
  - **Física de Segmentos, Partículas y *Screen Shake*:** Explosión de partículas al comer cada manzana, vibración de cámara al chocar y sonido retro sintetizado en memoria.
  - **Generación Segura de Comida:** Algoritmo que comprueba que la manzana pulsante nunca aparezca sobre la cabeza ni sobre ningún segmento del cuerpo de la serpiente.
  - **Máquina de Estados Finita e Interfaz Dual (Mouse + Teclado):** Control fluido entre `MENU`, `OPCIONES`, `JUGANDO`, `PAUSA` y `GAMEOVER` permitiendo elegir entre 3 niveles de velocidad (`Fácil`, `Normal`, `Difícil`) y 4 temas de color (`Verde Clásico`, `Azul Neón`, `Fuego`, `Morado Mágico`).

---

### 5. Menú Principal (Lobby Arcade en Pygame)

Orquestador visual a 60 FPS que centraliza el acceso a todos los juegos mediante una cuadrícula de cartuchos interactivos.

- **Dashboard Interactivo (`pygame`):** Fondo espacial animado con estrellas en movimiento, 4 tarjetas de juego con iconos vectoriales animados (`dibujar_icono_juego`), efectos *hover* y sonidos sintetizados de navegación.
- **Gestión Limpia de Ventanas y Consola:** Cierra su contexto gráfico (`pygame.quit()`) antes de ceder el control al juego elegido (ya sea otra ventana `pygame`, `turtle` o la consola interactiva de *El Ahorcado*), y se reabre automáticamente al finalizar cada partida.
- **Patrón Modular:** Aplica la convención estándar `from [paquete] import [módulo]` y la invocación uniforme de la interfaz pública `.jugar()`.
- **Guardia de Ejecución (`if __name__ == '__main__':`):** Garantiza que cada juego pueda ser ejecutado tanto de manera individual e independiente como a través del menú unificado.

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
   python -m serpiente.juego_serpiente
   ```

---

## 👨‍💻 Créditos y Reconocimientos

- **Desarrollador / Autor:** Estudiante de Lógica de Programación y Desarrollo de Software.
- **Curso:** _Fundamentos de Python 1_.
- **Instituciones Aliadas:** **Cisco Networking Academy** & **FUNDESTEAM Panamá**.
