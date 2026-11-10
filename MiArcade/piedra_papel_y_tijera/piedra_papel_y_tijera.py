import pygame
import random
import math
import array

def crear_sonido(frecuencia, duracion_ms, volumen=0.25):
    try:
        sample_rate = 44100
        n_samples = int(sample_rate * (duracion_ms / 1000.0))
        buf = array.array("h")
        for i in range(n_samples):
            t = float(i) / sample_rate
            envolvente = max(0.0, 1.0 - (i / n_samples))
            valor = int(32767.0 * volumen * envolvente * math.sin(2.0 * math.pi * frecuencia * t))
            buf.append(valor)
        return pygame.mixer.Sound(buffer=buf)
    except Exception:
        return None

def reproducir(sonido):
    if sonido is not None:
        try:
            sonido.play()
        except Exception:
            pass

def dibujar_icono(superficie, tipo, cx, cy, color_borde):
    pygame.draw.circle(superficie, (30, 32, 48), (cx, cy), 68)
    pygame.draw.circle(superficie, color_borde, (cx, cy), 68, 4)

    if tipo == "piedra":
        puntos = [
            (cx - 32, cy + 12),
            (cx - 36, cy - 12),
            (cx - 16, cy - 32),
            (cx + 14, cy - 34),
            (cx + 36, cy - 14),
            (cx + 32, cy + 18),
            (cx + 4, cy + 30)
        ]
        pygame.draw.polygon(superficie, (140, 150, 170), puntos)
        pygame.draw.polygon(superficie, (210, 220, 235), puntos, 3)
        pygame.draw.line(superficie, (190, 200, 215), (cx - 16, cy - 16), (cx + 8, cy - 18), 3)
        pygame.draw.line(superficie, (100, 110, 130), (cx - 12, cy + 10), (cx + 16, cy + 6), 3)

    elif tipo == "papel":
        rect_papel = pygame.Rect(cx - 28, cy - 36, 56, 72)
        pygame.draw.rect(superficie, (240, 245, 255), rect_papel, border_radius=6)
        pygame.draw.rect(superficie, (100, 180, 255), rect_papel, 3, border_radius=6)
        for i in range(-18, 26, 12):
            pygame.draw.line(superficie, (150, 175, 210), (cx - 16, cy + i), (cx + 16, cy + i), 3)

    elif tipo == "tijera":
        pygame.draw.line(superficie, (220, 225, 235), (cx - 18, cy + 18), (cx + 24, cy - 28), 7)
        pygame.draw.line(superficie, (220, 225, 235), (cx + 18, cy + 18), (cx - 24, cy - 28), 7)
        pygame.draw.circle(superficie, (100, 110, 130), (cx, cy - 4), 5)
        pygame.draw.circle(superficie, (255, 95, 120), (cx - 22, cy + 24), 14, 5)
        pygame.draw.circle(superficie, (255, 95, 120), (cx + 22, cy + 24), 14, 5)

    else:
        fuente_interrogacion = pygame.font.SysFont("Arial Black", 52, bold=True)
        txt = fuente_interrogacion.render("?", True, (130, 140, 165))
        superficie.blit(txt, txt.get_rect(center=(cx, cy)))

def jugar():
    pygame.init()
    try:
        pygame.mixer.init(frequency=44100, size=-16, channels=1)
    except Exception:
        pass

    snd_rebote = crear_sonido(340, 80, 0.2)
    snd_victoria = crear_sonido(660, 260, 0.3)
    snd_derrota = crear_sonido(180, 300, 0.3)
    snd_empate = crear_sonido(440, 160, 0.25)

    ANCHO, ALTO = 760, 620
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Piedra, Papel o Tijera - MiArcade (60 FPS)")
    reloj = pygame.time.Clock()

    fuente_titulo = pygame.font.SysFont("Arial Black", 28, bold=True)
    fuente_sub = pygame.font.SysFont("Arial", 18, bold=True)
    fuente_grande = pygame.font.SysFont("Arial Black", 24, bold=True)
    fuente_boton = pygame.font.SysFont("Arial", 18, bold=True)
    fuente_peq = pygame.font.SysFont("Arial", 14)

    victorias = 0
    derrotas = 0
    empates = 0
    ronda = 0

    opciones = ["piedra", "papel", "tijera"]
    nombres = {"piedra": "PIEDRA", "papel": "PAPEL", "tijera": "TIJERA", None: "ESPERANDO"}

    eleccion_jugador = None
    eleccion_cpu = None
    jugada_pendiente = None

    estado = "ESPERANDO"
    tiempo_inicio_anim = 0
    ultimo_rebote = -1

    mensaje_resultado = "¡Elige tu jugada o presiona 1, 2 o 3!"
    color_resultado = (220, 225, 240)

    particulas = []
    shake_frames = 0

    botones_jugada = [
        {"texto": "[1] Piedra", "valor": "piedra", "rect": pygame.Rect(110, 440, 160, 56), "color": (58, 134, 255)},
        {"texto": "[2] Papel", "valor": "papel", "rect": pygame.Rect(300, 440, 160, 56), "color": (131, 56, 236)},
        {"texto": "[3] Tijera", "valor": "tijera", "rect": pygame.Rect(490, 440, 160, 56), "color": (255, 0, 110)}
    ]

    btn_reiniciar = {"texto": "Reiniciar (R)", "rect": pygame.Rect(210, 535, 160, 42), "color": (255, 183, 3)}
    btn_salir = {"texto": "Menú (ESC)", "rect": pygame.Rect(390, 535, 160, 42), "color": (239, 71, 111)}

    def iniciar_duelo(jugada):
        nonlocal estado, jugada_pendiente, tiempo_inicio_anim, ultimo_rebote, mensaje_resultado, color_resultado
        if estado == "ANIMANDO":
            return
        jugada_pendiente = jugada
        estado = "ANIMANDO"
        tiempo_inicio_anim = pygame.time.get_ticks()
        ultimo_rebote = -1
        mensaje_resultado = "¡Piedra... Papel... o Tijera!"
        color_resultado = (255, 209, 102)

    def resolver_duelo():
        nonlocal victorias, derrotas, empates, ronda, eleccion_jugador, eleccion_cpu, estado
        nonlocal mensaje_resultado, color_resultado, shake_frames

        ronda += 1
        eleccion_jugador = jugada_pendiente
        eleccion_cpu = random.choice(opciones)
        estado = "RESULTADO"

        if eleccion_jugador == eleccion_cpu:
            empates += 1
            mensaje_resultado = "¡EMPATE EN ESTA RONDA!"
            color_resultado = (255, 209, 102)
            reproducir(snd_empate)
        elif (eleccion_jugador == "piedra" and eleccion_cpu == "tijera") or \
             (eleccion_jugador == "papel" and eleccion_cpu == "piedra") or \
             (eleccion_jugador == "tijera" and eleccion_cpu == "papel"):
            victorias += 1
            mensaje_resultado = "¡GANASTE ESTA RONDA!"
            color_resultado = (6, 214, 160)
            reproducir(snd_victoria)
            generar_confeti(ANCHO // 2, 240)
        else:
            derrotas += 1
            mensaje_resultado = "¡LA CPU GANÓ ESTA RONDA!"
            color_resultado = (239, 71, 111)
            shake_frames = 14
            reproducir(snd_derrota)

    def generar_confeti(x, y):
        colores = [(6, 214, 160), (255, 209, 102), (77, 243, 255), (255, 95, 162), (180, 255, 100)]
        for _ in range(55):
            angulo = random.uniform(0, 2 * math.pi)
            vel = random.uniform(2.5, 8.5)
            particulas.append({
                "x": float(x),
                "y": float(y),
                "vx": math.cos(angulo) * vel,
                "vy": math.sin(angulo) * vel - 2.0,
                "radio": random.randint(4, 7),
                "color": random.choice(colores),
                "vida": random.randint(35, 65)
            })

    def reiniciar_marcador():
        nonlocal victorias, derrotas, empates, ronda, eleccion_jugador, eleccion_cpu, estado, mensaje_resultado, color_resultado
        if estado == "ANIMANDO":
            return
        victorias = 0
        derrotas = 0
        empates = 0
        ronda = 0
        eleccion_jugador = None
        eleccion_cpu = None
        estado = "ESPERANDO"
        mensaje_resultado = "¡Marcador reiniciado! Elige tu jugada."
        color_resultado = (220, 225, 240)
        particulas.clear()

    ejecutando = True
    while ejecutando:
        pos_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False
                elif evento.key in (pygame.K_1, pygame.K_KP1):
                    iniciar_duelo("piedra")
                elif evento.key in (pygame.K_2, pygame.K_KP2):
                    iniciar_duelo("papel")
                elif evento.key in (pygame.K_3, pygame.K_KP3):
                    iniciar_duelo("tijera")
                elif evento.key == pygame.K_r:
                    reiniciar_marcador()
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                for b in botones_jugada:
                    if b["rect"].collidepoint(pos_mouse):
                        iniciar_duelo(b["valor"])
                if btn_reiniciar["rect"].collidepoint(pos_mouse):
                    reiniciar_marcador()
                elif btn_salir["rect"].collidepoint(pos_mouse):
                    ejecutando = False

        offset_y_anim = 0
        if estado == "ANIMANDO":
            transcurrido = pygame.time.get_ticks() - tiempo_inicio_anim
            paso_rebote = transcurrido // 220
            if paso_rebote > ultimo_rebote and paso_rebote < 3:
                ultimo_rebote = paso_rebote
                reproducir(snd_rebote)

            if transcurrido >= 680:
                resolver_duelo()
            else:
                offset_y_anim = int(math.sin(transcurrido * 0.028) * 24)

        ox, oy = 0, 0
        if shake_frames > 0:
            shake_frames -= 1
            ox = random.randint(-6, 6)
            oy = random.randint(-6, 6)

        pantalla.fill((18, 18, 24))

        txt_titulo = fuente_titulo.render("PIEDRA, PAPEL O TIJERA", True, (77, 243, 255))
        pantalla.blit(txt_titulo, txt_titulo.get_rect(center=(ANCHO // 2 + ox, 42 + oy)))

        rect_marcador = pygame.Rect(90 + ox, 78 + oy, ANCHO - 180, 44)
        pygame.draw.rect(pantalla, (30, 32, 44), rect_marcador, border_radius=10)
        pygame.draw.rect(pantalla, (60, 65, 90), rect_marcador, 2, border_radius=10)

        texto_marcador = f"Ronda: {ronda}     |     Tú: {victorias}     |     CPU: {derrotas}     |     Empates: {empates}"
        surf_marcador = fuente_sub.render(texto_marcador, True, (240, 245, 255))
        pantalla.blit(surf_marcador, surf_marcador.get_rect(center=rect_marcador.center))

        cx_jug, cy_jug = 220 + ox, 250 + oy + offset_y_anim
        cx_cpu, cy_cpu = 540 + ox, 250 + oy + offset_y_anim

        lbl_jug = fuente_sub.render("TÚ", True, (77, 243, 255))
        pantalla.blit(lbl_jug, lbl_jug.get_rect(center=(220 + ox, 152 + oy)))

        lbl_cpu = fuente_sub.render("CPU", True, (255, 107, 107))
        pantalla.blit(lbl_cpu, lbl_cpu.get_rect(center=(540 + ox, 152 + oy)))

        icono_mostrar_jug = None if estado == "ANIMANDO" else eleccion_jugador
        icono_mostrar_cpu = None if estado == "ANIMANDO" else eleccion_cpu

        dibujar_icono(pantalla, icono_mostrar_jug, cx_jug, cy_jug, (77, 243, 255))
        dibujar_icono(pantalla, icono_mostrar_cpu, cx_cpu, cy_cpu, (255, 107, 107))

        nom_jug = fuente_peq.render(nombres[icono_mostrar_jug], True, (180, 190, 210))
        pantalla.blit(nom_jug, nom_jug.get_rect(center=(220 + ox, 340 + oy)))

        nom_cpu = fuente_peq.render(nombres[icono_mostrar_cpu], True, (180, 190, 210))
        pantalla.blit(nom_cpu, nom_cpu.get_rect(center=(540 + ox, 340 + oy)))

        txt_vs = fuente_grande.render("VS", True, (255, 209, 102))
        pantalla.blit(txt_vs, txt_vs.get_rect(center=(ANCHO // 2 + ox, 250 + oy)))

        surf_res = fuente_grande.render(mensaje_resultado, True, color_resultado)
        pantalla.blit(surf_res, surf_res.get_rect(center=(ANCHO // 2 + ox, 392 + oy)))

        for b in botones_jugada:
            hover = b["rect"].collidepoint(pos_mouse) and estado != "ANIMANDO"
            rect_draw = b["rect"].inflate(6, 4) if hover else b["rect"]
            color_bg = tuple(min(255, c + 35) for c in b["color"]) if hover else b["color"]
            pygame.draw.rect(pantalla, color_bg, rect_draw, border_radius=12)
            pygame.draw.rect(pantalla, (255, 255, 255), rect_draw, 2, border_radius=12)
            txt_b = fuente_boton.render(b["texto"], True, (255, 255, 255))
            pantalla.blit(txt_b, txt_b.get_rect(center=rect_draw.center))

        for b_acc, color_txt in ((btn_reiniciar, (20, 20, 28)), (btn_salir, (255, 255, 255))):
            hover = b_acc["rect"].collidepoint(pos_mouse)
            rect_draw = b_acc["rect"].inflate(4, 2) if hover else b_acc["rect"]
            color_bg = tuple(min(255, c + 30) for c in b_acc["color"]) if hover else b_acc["color"]
            pygame.draw.rect(pantalla, color_bg, rect_draw, border_radius=8)
            txt_b = fuente_sub.render(b_acc["texto"], True, color_txt)
            pantalla.blit(txt_b, txt_b.get_rect(center=rect_draw.center))

        for p in particulas[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vy"] += 0.22
            p["vida"] -= 1
            if p["vida"] <= 0:
                particulas.remove(p)
            else:
                pygame.draw.circle(pantalla, p["color"], (int(p["x"]), int(p["y"])), p["radio"])

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    jugar()
