import turtle
import random
import time

# ==========================================
# CONFIGURACIÓN Y ESTADO DEL JUEGO
# ==========================================
# Estados: "MENU", "OPCIONES", "JUGANDO", "PAUSA", "GAMEOVER"
estado_juego = "MENU"

puntos = 0
record = 0

# Velocidades optimizadas para respuesta ágil y fluida
dificultades = {
    "Fácil": 0.11,     # Velocidad cómoda
    "Normal": 0.07,    # Velocidad ágil recomendada
    "Difícil": 0.04    # Velocidad rápida para expertos
}
dificultad_actual = "Normal"
velocidad_actual = dificultades[dificultad_actual]

# Cola de giros para que las teclas respondan de inmediato sin retraso
cola_direcciones = []
tiempo_ultimo_movimiento = 0.0

temas_color = [
    {"nombre": "Verde Clásico", "cabeza": "lime", "cuerpo": "forestgreen"},
    {"nombre": "Azul Neón", "cabeza": "cyan", "cuerpo": "dodgerblue"},
    {"nombre": "Fuego", "cabeza": "yellow", "cuerpo": "darkorange"},
    {"nombre": "Morado Mágico", "cabeza": "magenta", "cuerpo": "purple"}
]
indice_color = 0

# ==========================================
# CREAR LA VENTANA
# ==========================================
ventana = turtle.Screen()
ventana.title("Juego de la Serpiente - Snake Game")
ventana.bgcolor("#121212")  # Fondo oscuro de alto contraste
ventana.setup(650, 650)
ventana.tracer(0)

# ==========================================
# CREAR OBJETOS DEL JUEGO
# ==========================================
# Cabeza de la serpiente
serpiente = turtle.Turtle()
serpiente.speed(0)
serpiente.shape("square")
serpiente.color(temas_color[indice_color]["cabeza"])
serpiente.penup()
serpiente.goto(0, 0)
serpiente.direction = "quieta"
serpiente.hideturtle()

# Comida
comida = turtle.Turtle()
comida.speed(0)
comida.shape("circle")
comida.color("red")
comida.penup()
comida.goto(100, 100)
comida.hideturtle()

# Lista para los segmentos del cuerpo
cola = []

# Marcador de puntos
marcador = turtle.Turtle()
marcador.speed(0)
marcador.color("white")
marcador.hideturtle()
marcador.penup()
marcador.goto(0, 270)

# Pluma para dibujar la interfaz gráfica (menús y textos)
pluma_interfaz = turtle.Turtle()
pluma_interfaz.speed(0)
pluma_interfaz.color("white")
pluma_interfaz.hideturtle()
pluma_interfaz.penup()

# ==========================================
# FUNCIONES DE INTERFAZ Y PANTALLAS
# ==========================================
def mostrar_marcador():
    marcador.clear()
    marcador.write(f"Puntos: {puntos}    Récord: {record}    Nivel: {dificultad_actual}",
                   align="center",
                   font=("Arial", 14, "bold"))

def dibujar_menu():
    pluma_interfaz.clear()
    
    # Título principal
    pluma_interfaz.goto(0, 140)
    pluma_interfaz.color("lime") 
    pluma_interfaz.write("S N A K E   G A M E",
                         align="center",
                         font=("Arial Black", 30, "bold"))
    
    # Subtítulo
    pluma_interfaz.goto(0, 90)
    pluma_interfaz.color("white")
    pluma_interfaz.write("Proyecto de Lógica de Programación",
                         align="center",
                         font=("Arial", 13, "italic"))
    
    # Opciones de menú
    pluma_interfaz.goto(0, 0)
    pluma_interfaz.color("#4df3ff")
    pluma_interfaz.write("[ ESPACIO ]  Comenzar a Jugar",
                         align="center",
                         font=("Arial", 16, "bold"))
    
    pluma_interfaz.goto(0, -50)
    pluma_interfaz.color("#ffd166")
    pluma_interfaz.write("[ O ]  Opciones y Personalización",
                         align="center",
                         font=("Arial", 16, "bold"))

    pluma_interfaz.goto(0, -100)
    pluma_interfaz.color("#ff6b6b")
    pluma_interfaz.write("[ ESC ]  Salir del Juego",
                         align="center",
                         font=("Arial", 16, "bold"))

    # Récord actual
    pluma_interfaz.goto(0, -180)
    pluma_interfaz.color("lightgray")
    pluma_interfaz.write(f"Récord Actual: {record} pts",
                         align="center",
                         font=("Arial", 13, "normal"))

    # Controles
    pluma_interfaz.goto(0, -260)
    pluma_interfaz.color("gray")
    pluma_interfaz.write("Usa Flechas o W/A/S/D para moverte | P para Pausa",
                         align="center",
                         font=("Arial", 11, "normal"))

def dibujar_opciones():
    pluma_interfaz.clear()
    
    pluma_interfaz.goto(0, 160)
    pluma_interfaz.color("#ffd166")
    pluma_interfaz.write("OPCIONES DEL JUEGO",
                         align="center",
                         font=("Arial Black", 24, "bold"))

    # Dificultad
    pluma_interfaz.goto(0, 80)
    pluma_interfaz.color("white")
    pluma_interfaz.write("1. Dificultad (Velocidad):", align="center", font=("Arial", 15, "bold"))
    
    pluma_interfaz.goto(0, 45)
    color_dif = "lime" if dificultad_actual == "Fácil" else "gold" if dificultad_actual == "Normal" else "red"
    pluma_interfaz.color(color_dif)
    pluma_interfaz.write(f"-> Actual: {dificultad_actual} <-", align="center", font=("Arial", 14, "bold"))

    pluma_interfaz.goto(0, 15)
    pluma_interfaz.color("lightgray")
    pluma_interfaz.write("[ 1 ] Fácil    [ 2 ] Normal    [ 3 ] Difícil", align="center", font=("Arial", 12, "normal"))

    # Color de Serpiente
    pluma_interfaz.goto(0, -45)
    pluma_interfaz.color("white")
    pluma_interfaz.write("2. Color de la Serpiente:", align="center", font=("Arial", 15, "bold"))

    pluma_interfaz.goto(0, -80)
    pluma_interfaz.color(temas_color[indice_color]["cabeza"])
    pluma_interfaz.write(f"-> Color: {temas_color[indice_color]['nombre']} <-", align="center", font=("Arial", 14, "bold"))

    pluma_interfaz.goto(0, -110)
    pluma_interfaz.color("lightgray")
    pluma_interfaz.write("Presiona [ C ] para cambiar color", align="center", font=("Arial", 12, "normal"))

    # Regresar
    pluma_interfaz.goto(0, -200)
    pluma_interfaz.color("#4df3ff")
    pluma_interfaz.write("Presiona [ M ] o [ ESC ] para volver al Menú", align="center", font=("Arial", 14, "bold"))

def mostrar_pantalla_pausa():
    pluma_interfaz.clear()
    pluma_interfaz.goto(0, 20)
    pluma_interfaz.color("yellow")
    pluma_interfaz.write("J U E G O   E N   P A U S A",
                         align="center",
                         font=("Arial Black", 24, "bold"))
    
    pluma_interfaz.goto(0, -30)
    pluma_interfaz.color("white")
    pluma_interfaz.write("Presiona [ P ] para continuar o [ M ] para ir al Menú",
                         align="center",
                         font=("Arial", 13, "normal"))

def mostrar_game_over():
    pluma_interfaz.clear()
    pluma_interfaz.goto(0, 30)
    pluma_interfaz.color("red")
    pluma_interfaz.write("¡ G A M E   O V E R !",
                         align="center",
                         font=("Arial Black", 28, "bold"))
    
    pluma_interfaz.goto(0, -20)
    pluma_interfaz.color("white")
    pluma_interfaz.write(f"Puntuación final: {puntos}   |   Récord: {record}",
                         align="center",
                         font=("Arial", 14, "bold"))

    pluma_interfaz.goto(0, -70)
    pluma_interfaz.color("#4df3ff")
    pluma_interfaz.write("Presiona [ ESPACIO ] para reintentar o [ M ] para el Menú",
                         align="center",
                         font=("Arial", 13, "normal"))

# ==========================================
# GESTIÓN DE ACCIONES Y MENÚS
# ==========================================
def iniciar_juego():
    global estado_juego, puntos, tiempo_ultimo_movimiento
    estado_juego = "JUGANDO"
    pluma_interfaz.clear()
    cola_direcciones.clear()
    
    puntos = 0
    serpiente.color(temas_color[indice_color]["cabeza"])
    serpiente.goto(0, 0)
    serpiente.direction = "quieta"
    serpiente.showturtle()
    
    colocar_comida()
    comida.showturtle()

    for parte in cola:
        parte.hideturtle()
    cola.clear()

    mostrar_marcador()
    tiempo_ultimo_movimiento = time.time()

def abrir_opciones():
    global estado_juego
    if estado_juego in ["MENU", "GAMEOVER"]:
        estado_juego = "OPCIONES"
        marcador.clear()
        serpiente.hideturtle()
        comida.hideturtle()
        dibujar_opciones()

def regresar_al_menu():
    global estado_juego, puntos, record
    if puntos > record:
        record = puntos

    estado_juego = "MENU"
    cola_direcciones.clear()
    marcador.clear()
    serpiente.hideturtle()
    comida.hideturtle()
    for parte in cola:
        parte.hideturtle()
    cola.clear()
    
    dibujar_menu()

def pausar_reanudar():
    global estado_juego
    if estado_juego == "JUGANDO":
        estado_juego = "PAUSA"
        mostrar_pantalla_pausa()
    elif estado_juego == "PAUSA":
        estado_juego = "JUGANDO"
        pluma_interfaz.clear()

def accion_espacio():
    if estado_juego in ["MENU", "GAMEOVER"]:
        iniciar_juego()

def salir_juego():
    if estado_juego == "OPCIONES":
        regresar_al_menu()
    elif estado_juego == "MENU":
        ventana.bye()

def set_dificultad_facil():
    global dificultad_actual, velocidad_actual
    if estado_juego == "OPCIONES":
        dificultad_actual = "Fácil"
        velocidad_actual = dificultades["Fácil"]
        dibujar_opciones()

def set_dificultad_normal():
    global dificultad_actual, velocidad_actual
    if estado_juego == "OPCIONES":
        dificultad_actual = "Normal"
        velocidad_actual = dificultades["Normal"]
        dibujar_opciones()

def set_dificultad_dificil():
    global dificultad_actual, velocidad_actual
    if estado_juego == "OPCIONES":
        dificultad_actual = "Difícil"
        velocidad_actual = dificultades["Difícil"]
        dibujar_opciones()

def cambiar_color_serpiente():
    global indice_color
    if estado_juego == "OPCIONES":
        indice_color = (indice_color + 1) % len(temas_color)
        dibujar_opciones()

def colocar_comida():
    x = random.randint(-13, 13) * 20
    y = random.randint(-13, 13) * 20
    comida.goto(x, y)

# ==========================================
# SISTEMA DE ENTRADA ULTRA-RÁPIDO (SIN INPUT LAG)
# ==========================================
def registrar_direccion(nueva_dir):
    """
    Registra la dirección en una cola inmediata para que ninguna pulsación
    se pierda y el teclado responda con latencia cero.
    """
    if estado_juego != "JUGANDO":
        return

    opuestos = {
        "arriba": "abajo",
        "abajo": "arriba",
        "izquierda": "derecha",
        "derecha": "izquierda"
    }

    # Dirección de referencia: el último giro encolado o la dirección actual
    dir_referencia = cola_direcciones[-1] if cola_direcciones else serpiente.direction

    # Si la serpiente está detenida al inicio, arrancar en esa dirección de inmediato
    if serpiente.direction == "quieta":
        serpiente.direction = nueva_dir
        cola_direcciones.clear()
        return

    # Evitar giros opuestos directos (180 grados) y guardar máximo 2 giros anticipados
    if nueva_dir != dir_referencia and nueva_dir != opuestos.get(dir_referencia):
        if len(cola_direcciones) < 2:
            cola_direcciones.append(nueva_dir)

def subir():
    registrar_direccion("arriba")

def bajar():
    registrar_direccion("abajo")

def izquierda():
    registrar_direccion("izquierda")

def derecha():
    registrar_direccion("derecha")

def mover():
    if serpiente.direction == "arriba":
        serpiente.sety(serpiente.ycor() + 20)
    elif serpiente.direction == "abajo":
        serpiente.sety(serpiente.ycor() - 20)
    elif serpiente.direction == "izquierda":
        serpiente.setx(serpiente.xcor() - 20)
    elif serpiente.direction == "derecha":
        serpiente.setx(serpiente.xcor() + 20)

# ==========================================
# ASIGNACIÓN DE TECLAS
# ==========================================
ventana.listen()

# Flechas del teclado
ventana.onkeypress(subir, "Up")
ventana.onkeypress(bajar, "Down")
ventana.onkeypress(izquierda, "Left")
ventana.onkeypress(derecha, "Right")

# Teclas WASD (minúsculas y mayúsculas)
ventana.onkeypress(subir, "w")
ventana.onkeypress(bajar, "s")
ventana.onkeypress(izquierda, "a")
ventana.onkeypress(derecha, "d")
ventana.onkeypress(subir, "W")
ventana.onkeypress(bajar, "S")
ventana.onkeypress(izquierda, "A")
ventana.onkeypress(derecha, "D")

# Navegación y menús
ventana.onkeypress(accion_espacio, "space")
ventana.onkeypress(accion_espacio, "Return")
ventana.onkeypress(abrir_opciones, "o")
ventana.onkeypress(abrir_opciones, "O")
ventana.onkeypress(regresar_al_menu, "m")
ventana.onkeypress(regresar_al_menu, "M")
ventana.onkeypress(pausar_reanudar, "p")
ventana.onkeypress(pausar_reanudar, "P")
ventana.onkeypress(salir_juego, "Escape")

# Ajustes en menú de opciones
ventana.onkeypress(set_dificultad_facil, "1")
ventana.onkeypress(set_dificultad_normal, "2")
ventana.onkeypress(set_dificultad_dificil, "3")
ventana.onkeypress(cambiar_color_serpiente, "c")
ventana.onkeypress(cambiar_color_serpiente, "C")

# ==========================================
# LÓGICA DE CADA PASO DE LA SERPIENTE
# ==========================================
def paso_de_juego():
    global puntos, record, estado_juego

    # Si aún no se ha presionado ninguna tecla de dirección, permanecer quieta
    if serpiente.direction == "quieta":
        return

    # Si hay un giro pendiente en la cola de teclado, aplicarlo ahora
    if cola_direcciones:
        serpiente.direction = cola_direcciones.pop(0)

    # 1. Colisión con los bordes
    if abs(serpiente.xcor()) > 280 or abs(serpiente.ycor()) > 280:
        if puntos > record:
            record = puntos
        estado_juego = "GAMEOVER"
        mostrar_game_over()
        return

    # 2. Comer la comida
    if serpiente.distance(comida) < 20:
        colocar_comida()

        parte = turtle.Turtle()
        parte.speed(0)
        parte.shape("square")
        parte.color(temas_color[indice_color]["cuerpo"])
        parte.penup()
        cola.append(parte)

        puntos += 1
        if puntos > record:
            record = puntos
        mostrar_marcador()

    # 3. Mover los segmentos del cuerpo
    for i in range(len(cola) - 1, 0, -1):
        cola[i].goto(cola[i - 1].pos())

    if len(cola) > 0:
        cola[0].goto(serpiente.pos())

    # 4. Mover la cabeza
    mover()

    # 5. Colisión con el cuerpo
    for parte in cola:
        if serpiente.distance(parte) < 15:
            if puntos > record:
                record = puntos
            estado_juego = "GAMEOVER"
            mostrar_game_over()
            return

# ==========================================
# BUCLE PRINCIPAL (ALTA TASA DE RESPUESTA)
# ==========================================
dibujar_menu()

try:
    while True:
        # Se actualiza la ventana continuamente (200 veces por segundo)
        # para que las teclas se detecten con latencia de apenas ~5ms
        ventana.update()
        tiempo_actual = time.time()

        if estado_juego == "JUGANDO":
            # La serpiente solo avanza cuando se cumple su intervalo de velocidad
            if tiempo_actual - tiempo_ultimo_movimiento >= velocidad_actual:
                tiempo_ultimo_movimiento = tiempo_actual
                paso_de_juego()

        # Pausa mínima de 5 milisegundos para no saturar el procesador
        # sin bloquear la respuesta inmediata del teclado
        time.sleep(0.005)

except (turtle.Terminator, Exception):
    pass
