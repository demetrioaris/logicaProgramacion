# 🕹️ MiArcade - Virtual Game Hub

[![Python](https://img.shields.io/badge/Python-3.8+-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Pygame](https://img.shields.io/badge/Pygame-2D_Arcade-00B050?style=for-the-badge&logo=python&logoColor=white)](https://www.pygame.org/)
[![Cisco Networking Academy](https://img.shields.io/badge/Cisco_Networking_Academy-Course_Project-049fd9?style=for-the-badge&logo=cisco&logoColor=white)](https://www.netacad.com/)
[![FUNDESTEAM](https://img.shields.io/badge/FUNDESTEAM-Panamá-FF6F00?style=for-the-badge)](https://fundesteam.org/)
[![AI-Assisted](https://img.shields.io/badge/Development-AI--Assisted-8A2BE2?style=for-the-badge&logo=openai&logoColor=white)]()
[![Status](https://img.shields.io/badge/Status-Completed-success?style=for-the-badge)]()

> **MiArcade** es un ecosistema de minijuegos retro interactivos desarrollados en **Python** mediante la biblioteca gráfica **Pygame**. Diseñado bajo estándares de ingeniería de software, este proyecto combina **lógica algorítmica, programación estructurada, modularización desacoplada, gestión robusta de excepciones, arte vectorial procedural y audio sintetizado en tiempo real**, ofreciendo una experiencia fluida controlada tanto por mouse como por teclado.

---

## 📌 Contexto Institucional y Metodología

Este proyecto fue desarrollado en el marco del programa formativo **"Fundamentos de Python 1"**, promovido conjuntamente por **Cisco Networking Academy** y **FUNDESTEAM Panamá**.

Asimismo, la arquitectura, modernización gráfica y optimización de algoritmos contaron con el **apoyo de herramientas de Inteligencia Artificial (IA)** como asistente de desarrollo y pair programming, permitiendo refactorizar código monolítico hacia una arquitectura modular, acelerar la implementación de matemáticas procedurales y elevar la calidad global del producto.

---

## 🎯 Competencias Técnicas Adquiridas

El desarrollo del proyecto consolida cinco áreas clave de la ingeniería de software:

- **Bloque 1: Fundamentos del Lenguaje y Control de Eventos**
  - Sintaxis estricta, semántica y modelo de ejecución de Python.
  - Flujo lógico estructurado, literales, variables y captura asíncrona de eventos de entrada (`pygame.event`) para periféricos (teclado y ratón).
  - Depuración proactiva de errores en tiempo de ejecución.

- **Bloque 2: Tipos de Datos y Operaciones Aritmético-Lógicas**
  - Manipulación estricta de tipos de datos (`int`, `float`, `str`, `bool`) y conversiones seguras.
  - Modelado matemático: trigonometría (`math.sin`, `math.pi`) para animaciones sinusoidales y precedencia de operadores.
  - Normalización y saneamiento léxico de texto (`.strip()`, `.upper()`, `str.maketrans`).

- **Bloque 3: Flujo de Control y Arquitectura de Game Loop**
  - Bifurcaciones exhaustivas (`if`, `elif`, `else`) y máquinas de estados finitas (`MENU`, `JUGANDO`, `PAUSA`, `GAMEOVER`).
  - Ciclos de vida interactivos (`while`, `for`) gestionados a tasa constante mediante reloj interno (`pygame.time.Clock`).
  - Control de iteraciones con directivas `break` y `continue`.

- **Bloque 4: Estructuras de Datos, Modularización y Robustez**
  - Manejo de estructuras de datos: listas dinámicas, colas FIFO para entradas, tuplas inmutables, diccionarios y conjuntos (`set`) con búsquedas en $\mathcal{O}(1)$.
  - Arquitectura desacoplada en funciones y paquetes de Python, garantizando alta cohesión y bajo acoplamiento.
  - Manejo preventivo de excepciones (`try`, `except`, `else`, `raise`) para garantizar tolerancia a fallos.

- **Bloque 5: Gráficos 2D Procedurales y Síntesis de Sonido**
  - Renderizado vectorial con primitivas geométricas (`pygame.draw`), prescindiendo de dependencias de activos externos pesados.
  - Detección de colisiones (`Rect.collidepoint`), efectos dinámicos de cursor (*hover*), sistemas de partículas y vibración de pantalla (*screen shake*).
  - Generación algorítmica de ondas de audio retro de 8 bits en memoria con `array` y reproducción con `pygame.mixer.Sound`.

---

## 📁 Arquitectura del Proyecto

El repositorio implementa una estructura modular organizada en módulos temáticos e independientes:

```text
MiArcade/
│
├── menu_principal.py               # Orquestador del Arcade y lanzador interactivo
│
├── piedra_papel_y_tijera/          # Módulo: Juego 1
│   └── piedra_papel_y_tijera.py    # Duelo clásico con física de partículas y marcadores
│
├── cazafantasma/                   # Módulo: Juego 2 (Simulación de Caso de Negocio)
│   └── cazafantasmas.py            # Entrenador aritmético gamificado para niños
│
├── ahorcado/                       # Módulo: Juego 3
│   ├── ahorcado.py                 # Juego de palabras con teclado virtual e interfaz gráfica
│   └── palabras.py                 # Banco léxico desacoplado
│
└── serpiente/                      # Módulo: Juego 4
    └── juego_serpiente.py          # Motor Snake clásico con cola anti-lag y personalización
```

---

## 🎮 Catálogo de Juegos y Demostración Técnica

### 1. Piedra, Papel o Tijera

Reinvención visual interactiva del duelo tradicional contra la computadora.

- **Detalles de Implementación:**
  - **Gráficos Vectoriales Procedurales:** Dibujo en código de piedra, papel y tijera usando polígonos, círculos y líneas.
  - **Animación Sinusoidal:** Oscilación rítmica previa al enfrentamiento para aumentar el dinamismo visual.
  - **Efectos Visuales y Sonoros:** Explosión de confeti basada en física de partículas al ganar y sacudida de pantalla al perder.
  - **Audio 8-bits:** Ondas de audio sintetizadas matemáticamente en memoria sin requerir archivos de sonido externos.
  - **Control Híbrido:** Interacción fluida mediante clics o teclas rápidas (`1`, `2`, `3`, `R`, `ESC`).

---

### 2. Cazafantasmas Matemático

> 💼 **Simulación de Caso Corporativo:**  
> Proyecto desarrollado bajo la premisa de un requerimiento institucional educativo: crear un videojuego ágil y motivador para reforzar la agilidad mental y aritmética en infantes de primaria.

- **Detalles de Implementación:**
  - **Mecánica Accesible para Niños:** Permite responder seleccionando una de las 4 tarjetas en pantalla o tecleando la solución y pulsando `ENTER`.
  - **Fantasmas Levitantes:** Animaciones calculadas proceduralmente con expresiones reactivas ante impactos.
  - **Aritmética Adaptada:** Generación controlada de operaciones: sumas, restas sin valores negativos y divisiones exactas.
  - **Efectos Especiales:** Láser de protones, dispersión de ectoplasma y seguimiento de salud mediante corazones vectoriales.
  - **Protección Antierror:** Validación defensiva con captura de excepciones (`ValueError`) que activa un escudo protector sin penalizar vidas infantiles por pulsar caracteres accidentales.

---

### 3. El Ahorcado

Versión moderna del clásico juego de adivinanza léxica enriquecido con componentes visuales adaptativos.

- **Detalles de Implementación:**
  - **Teclado Virtual Dual:** Panel táctil en pantalla de 26 letras con retroalimentación cromática (verde para aciertos, rojo oscuro para intentos fallidos), operable simultáneamente con el teclado del ordenador.
  - **Construcción Vectorial Progresiva:** Ilustración por etapas de la horca y el personaje correspondiente al conteo de vidas restantes.
  - **Optimización con Conjuntos (`set`):** Búsqueda instantánea de letras acertadas y usadas en tiempo constante $\mathcal{O}(1)$.
  - **Normalización Automática:** Tratamiento de tildes y caracteres especiales con tablas de traducción para garantizar compatibilidad léxica.

---

### 4. La Serpiente (Snake)

Recreación fiel y refinada del clásico de arcade con controles responsivos y configuración visual.

- **Detalles de Implementación:**
  - **Tablero Ajedrezado (28×22):** Cuadrícula con alternancia sutil de contraste para guiar la percepción espacial.
  - **Cola FIFO Anti-Lag:** Búfer de entradas que registra giros inmediatos, evitando colisiones accidentales de 180° y retrasos de respuesta.
  - **Generación Segura de Manzanas:** Algoritmo que previene el desove de comida sobre el cuerpo o la cabeza de la serpiente.
  - **Personalización y Dificultad:** Soporte para 3 niveles de velocidad y 4 temas cromáticos (Verde Clásico, Azul Neón, Fuego y Morado Mágico).

---

### 5. Menú Principal (Hub Central)

Lobby interactivo que centraliza y orquesta la ejecución de los diferentes minijuegos.

- **Detalles de Implementación:**
  - **Interfaz Atractiva:** Fondo estelar en movimiento continuo, cartuchos virtuales con iluminación dinámica y previsualizaciones animadas.
  - **Gestión Limpia de Contextos:** Cierre y reapertura controlada de instancias gráficas para alternar de juego sin conflictos de recursos.
  - **Modularidad:** Punto de entrada limpio que invoca el método estandarizado `.jugar()` de cada paquete.

---

## 🚀 Instalación y Ejecución

### Prerrequisitos

1. **Python 3.8+** instalado en el sistema:
   ```bash
   python --version
   ```

2. Instalar la dependencia gráfica **Pygame**:
   ```bash
   pip install pygame
   ```

### Puesta en Marcha

1. Clonar el repositorio y acceder al directorio del proyecto:
   ```bash
   git clone https://github.com/tu-usuario/MiArcade.git
   cd MiArcade
   ```

2. Lanzar la consola Arcade:
   ```bash
   python menu_principal.py
   ```

3. *(Opcional)* Ejecutar módulos individuales de forma directa:
   ```bash
   python -m piedra_papel_y_tijera.piedra_papel_y_tijera
   python -m cazafantasma.cazafantasmas
   python -m ahorcado.ahorcado
   python -m serpiente.juego_serpiente
   ```

---

## 👨‍💻 Créditos y Reconocimientos

- **Desarrollador / Autor:** Estudiante del área de Informática Aplicada a la Educación / Lógica de Programación.
- **Asistencia Técnica:** Inteligencia Artificial (AI-Assisted Development) aplicada al diseño algorítmico, modularización y optimización matemática.
- **Curso:** _Fundamentos de Python 1_.
- **Instituciones Promotoras:** **Cisco Networking Academy** & **FUNDESTEAM Panamá**.
