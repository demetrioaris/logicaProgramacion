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

def dibujar_corazon(superficie, x, y, activo=True):
    color = (255, 65, 108) if activo else (55, 58, 75)
    pygame.draw.circle(superficie, color, (x - 7, y - 4), 8)
    pygame.draw.circle(superficie, color, (x + 7, y - 4), 8)
    puntos = [(x - 15, y - 1), (x + 15, y - 1), (x, y + 15)]
    pygame.draw.polygon(superficie, color, puntos)

def dibujar_fantasma(superficie, cx, cy, color_cuerpo, tiempo_ms, atrapado=False):
    onda = int(math.sin(tiempo_ms * 0.006) * 10)
    cy_anim = cy + onda

    pygame.draw.circle(superficie, (30, 55, 65), (cx, cy_anim), 72, 3)
    pygame.draw.circle(superficie, color_cuerpo, (cx, cy_anim - 12), 46)
    rect_cuerpo = pygame.Rect(cx - 46, cy_anim - 12, 92, 48)
    pygame.draw.rect(superficie, color_cuerpo, rect_cuerpo)

    ancho_pico = 23
    for i in range(4):
        px = cx - 46 + i * ancho_pico
        onda_pico = int(math.sin(tiempo_ms * 0.012 + i) * 4)
        puntos_falda = [
            (px, cy_anim + 35),
            (px + ancho_pico, cy_anim + 35),
            (px + ancho_pico // 2, cy_anim + 52 + onda_pico)
        ]
        pygame.draw.polygon(superficie, color_cuerpo, puntos_falda)

    pygame.draw.circle(superficie, (255, 255, 255), (cx - 16, cy_anim - 14), 12)
    pygame.draw.circle(superficie, (255, 255, 255), (cx + 16, cy_anim - 14), 12)

    color_pupila = (255, 60, 60) if atrapado else (20, 24, 40)
    pygame.draw.circle(superficie, color_pupila, (cx - 14, cy_anim - 14), 6)
    pygame.draw.circle(superficie, color_pupila, (cx + 18, cy_anim - 14), 6)

    if atrapado:
        pygame.draw.circle(superficie, (20, 24, 40), (cx, cy_anim + 12), 10)
    else:
        pygame.draw.arc(superficie, (20, 24, 40), (cx - 14, cy_anim + 2, 28, 16), math.pi, 2 * math.pi, 4)

def generar_operacion():
    op = random.choice(["+", "-", "*", "/"])
    if op == "+":
        n1 = random.randint(1, 15)
        n2 = random.randint(1, 15)
        solucion = n1 + n2
    elif op == "-":
        n1 = random.randint(5, 20)
        n2 = random.randint(1, n1)
        solucion = n1 - n2
    elif op == "*":
        n1 = random.randint(1, 10)
        n2 = random.randint(1, 10)
        solucion = n1 * n2
    else:
        n2 = random.randint(1, 10)
        solucion = random.randint(1, 10)
        n1 = n2 * solucion

    simbolo = "÷" if op == "/" else ("x" if op == "*" else op)
    pregunta = f"¿Cuánto es  {n1} {simbolo} {n2} ?"

    opciones = {solucion}
    while len(opciones) < 4:
        desvio = random.choice([-5, -3, -2, -1, 1, 2, 3, 4, 5, 6])
        candidato = max(0, solucion + desvio)
        opciones.add(candidato)

    lista_opciones = list(opciones)
    random.shuffle(lista_opciones)
    return pregunta, solucion, lista_opciones

def jugar():
    pygame.init()
    try:
        pygame.mixer.init(frequency=44100, size=-16, channels=1)
    except Exception:
        pass

    snd_laser = crear_sonido(740, 220, 0.3)
    snd_error = crear_sonido(175, 280, 0.3)
    snd_escudo = crear_sonido(420, 140, 0.25)
    snd_victoria = crear_sonido(880, 350, 0.3)

    ANCHO, ALTO = 780, 640
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("Cazafantasmas Matemático - MiArcade (60 FPS)")
    reloj = pygame.time.Clock()

    fuente_titulo = pygame.font.SysFont("Arial Black", 25, bold=True)
    fuente_pregunta = pygame.font.SysFont("Arial Black", 28, bold=True)
    fuente_sub = pygame.font.SysFont("Arial", 18, bold=True)
    fuente_opcion = pygame.font.SysFont("Arial Black", 22, bold=True)
    fuente_peq = pygame.font.SysFont("Arial", 15, bold=True)

    colores_fantasma = [
        (100, 240, 255),
        (180, 130, 255),
        (120, 255, 160),
        (255, 150, 210),
        (255, 210, 110)
    ]

    vidas = 3
    puntos = 0
    ronda = 1
    total_rondas = 5
    estado = "JUGANDO"

    pregunta_actual, solucion_actual, opciones_actuales = generar_operacion()
    color_fantasma_actual = random.choice(colores_fantasma)
    texto_entrada = ""

    mensaje_feedback = "¡Elige una tarjeta o escribe el número y presiona ENTER!"
    color_feedback = (200, 215, 245)

    tiempo_efecto = 0
    acierto_reciente = False
    shake_frames = 0
    particulas = []

    rects_opciones = [
        pygame.Rect(110, 445, 125, 64),
        pygame.Rect(255, 445, 125, 64),
        pygame.Rect(400, 445, 125, 64),
        pygame.Rect(545, 445, 125, 64)
    ]

    btn_disparar = pygame.Rect(475, 368, 150, 46)
    btn_reiniciar = pygame.Rect(210, 565, 170, 44)
    btn_salir = pygame.Rect(400, 565, 170, 44)

    def lanzar_particulas(x, y, color_base):
        for _ in range(50):
            ang = random.uniform(0, 2 * math.pi)
            vel = random.uniform(2.0, 8.0)
            particulas.append({
                "x": float(x),
                "y": float(y),
                "vx": math.cos(ang) * vel,
                "vy": math.sin(ang) * vel - 1.5,
                "radio": random.randint(4, 8),
                "color": color_base if random.random() > 0.35 else (255, 255, 160),
                "vida": random.randint(30, 55)
            })

    def procesar_disparo(valor_texto):
        nonlocal puntos, vidas, estado, tiempo_efecto, acierto_reciente
        nonlocal mensaje_feedback, color_feedback, shake_frames, texto_entrada

        if estado != "JUGANDO":
            return

        try:
            if not valor_texto.strip():
                raise ValueError("Escribe un número o haz clic en una tarjeta.")
            disparo = int(valor_texto.strip())
        except ValueError:
            mensaje_feedback = "🛡️ [ESCUDO ACTIVO] ¡Escribe solo números o toca una tarjeta!"
            color_feedback = (255, 209, 102)
            texto_entrada = ""
            reproducir(snd_escudo)
        else:
            texto_entrada = str(disparo)
            estado = "EFECTO"
            tiempo_efecto = pygame.time.get_ticks()

            if disparo == solucion_actual:
                puntos += 10
                acierto_reciente = True
                mensaje_feedback = "🎉 ¡ZAP! ¡Excelente disparo, atrapaste al fantasma! (+10 pts)"
                color_feedback = (6, 214, 160)
                reproducir(snd_laser)
                lanzar_particulas(ANCHO // 2, 225, color_fantasma_actual)
            else:
                vidas -= 1
                acierto_reciente = False
                mensaje_feedback = f"💨 ¡El fantasma esquivó el rayo! La respuesta era {solucion_actual}."
                color_feedback = (239, 71, 111)
                shake_frames = 14
                reproducir(snd_error)

    def avanzar_ronda():
        nonlocal ronda, estado, pregunta_actual, solucion_actual, opciones_actuales
        nonlocal color_fantasma_actual, texto_entrada, mensaje_feedback, color_feedback

        ronda += 1
        texto_entrada = ""
        if vidas <= 0 or ronda > total_rondas:
            estado = "FIN"
            if vidas > 0:
                reproducir(snd_victoria)
        else:
            estado = "JUGANDO"
            pregunta_actual, solucion_actual, opciones_actuales = generar_operacion()
            color_fantasma_actual = random.choice(colores_fantasma)
            mensaje_feedback = "¡Apareció otro fantasma! Resuelve la operación:"
            color_feedback = (200, 215, 245)

    def reiniciar_mision():
        nonlocal vidas, puntos, ronda, estado, pregunta_actual, solucion_actual, opciones_actuales
        nonlocal color_fantasma_actual, texto_entrada, mensaje_feedback, color_feedback
        vidas = 3
        puntos = 0
        ronda = 1
        estado = "JUGANDO"
        pregunta_actual, solucion_actual, opciones_actuales = generar_operacion()
        color_fantasma_actual = random.choice(colores_fantasma)
        texto_entrada = ""
        mensaje_feedback = "¡Nueva misión iniciada! Atrapa a los 5 fantasmas."
        color_feedback = (200, 215, 245)
        particulas.clear()

    ejecutando = True
    while ejecutando:
        ahora = pygame.time.get_ticks()
        pos_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False
                elif estado == "FIN" and evento.key in (pygame.K_SPACE, pygame.K_RETURN, pygame.K_r):
                    reiniciar_mision()
                elif estado == "JUGANDO":
                    if evento.key in (pygame.K_RETURN, pygame.K_KP_ENTER):
                        procesar_disparo(texto_entrada)
                    elif evento.key == pygame.K_BACKSPACE:
                        texto_entrada = texto_entrada[:-1]
                    elif len(texto_entrada) < 4 and evento.unicode.isprintable():
                        texto_entrada += evento.unicode
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if btn_reiniciar.collidepoint(pos_mouse):
                    reiniciar_mision()
                elif btn_salir.collidepoint(pos_mouse):
                    ejecutando = False
                elif estado == "JUGANDO":
                    if btn_disparar.collidepoint(pos_mouse):
                        procesar_disparo(texto_entrada)
                    for i, rect_op in enumerate(rects_opciones):
                        if rect_op.collidepoint(pos_mouse):
                            procesar_disparo(str(opciones_actuales[i]))

        if estado == "EFECTO" and ahora - tiempo_efecto >= 1050:
            avanzar_ronda()

        ox, oy = 0, 0
        if shake_frames > 0:
            shake_frames -= 1
            ox = random.randint(-6, 6)
            oy = random.randint(-6, 6)

        pantalla.fill((15, 18, 28))

        txt_titulo = fuente_titulo.render("CAZAFANTASMAS MATEMÁTICO", True, (100, 240, 255))
        pantalla.blit(txt_titulo, txt_titulo.get_rect(center=(ANCHO // 2 + ox, 34 + oy)))

        rect_hud = pygame.Rect(60 + ox, 64 + oy, ANCHO - 120, 46)
        pygame.draw.rect(pantalla, (26, 30, 46), rect_hud, border_radius=10)
        pygame.draw.rect(pantalla, (55, 65, 95), rect_hud, 2, border_radius=10)

        lbl_vidas = fuente_sub.render("Vidas:", True, (240, 245, 255))
        pantalla.blit(lbl_vidas, (85 + ox, 76 + oy))
        for i in range(3):
            dibujar_corazon(pantalla, 165 + i * 36 + ox, 87 + oy, activo=(i < vidas))

        ronda_mostrar = min(ronda, total_rondas)
        surf_info = fuente_sub.render(f"Puntos: {puntos}        |        Fantasma: {ronda_mostrar} de {total_rondas}", True, (255, 215, 100))
        pantalla.blit(surf_info, (320 + ox, 76 + oy))

        if estado in ("JUGANDO", "EFECTO"):
            if estado == "EFECTO" and acierto_reciente:
                pygame.draw.line(pantalla, (0, 255, 200), (ANCHO // 2, 370), (ANCHO // 2, 220), 10)
                pygame.draw.line(pantalla, (255, 255, 255), (ANCHO // 2, 370), (ANCHO // 2, 220), 4)

            dibujar_fantasma(pantalla, ANCHO // 2 + ox, 200 + oy, color_fantasma_actual, ahora, atrapado=(estado == "EFECTO" and acierto_reciente))

            rect_preg = pygame.Rect(160 + ox, 285 + oy, ANCHO - 320, 52)
            pygame.draw.rect(pantalla, (28, 34, 54), rect_preg, border_radius=12)
            pygame.draw.rect(pantalla, color_fantasma_actual, rect_preg, 2, border_radius=12)

            surf_preg = fuente_pregunta.render(pregunta_actual, True, (255, 255, 255))
            pantalla.blit(surf_preg, surf_preg.get_rect(center=rect_preg.center))

            lbl_escribe = fuente_peq.render("Escribe tu respuesta:", True, (180, 195, 220))
            pantalla.blit(lbl_escribe, (155 + ox, 381 + oy))

            rect_input = pygame.Rect(330 + ox, 368 + oy, 130, 46)
            pygame.draw.rect(pantalla, (20, 24, 38), rect_input, border_radius=8)
            pygame.draw.rect(pantalla, (100, 240, 255), rect_input, 2, border_radius=8)

            cursor = "|" if (ahora // 450) % 2 == 0 and estado == "JUGANDO" else ""
            surf_input = fuente_opcion.render(texto_entrada + cursor, True, (255, 255, 255))
            pantalla.blit(surf_input, surf_input.get_rect(center=rect_input.center))

            hover_disp = btn_disparar.collidepoint(pos_mouse) and estado == "JUGANDO"
            color_disp = (30, 215, 160) if hover_disp else (6, 180, 130)
            pygame.draw.rect(pantalla, color_disp, btn_disparar.move(ox, oy), border_radius=8)
            surf_disp = fuente_sub.render("⚡ DISPARAR", True, (15, 20, 30))
            pantalla.blit(surf_disp, surf_disp.get_rect(center=btn_disparar.move(ox, oy).center))

            for i, rect_op in enumerate(rects_opciones):
                hover = rect_op.collidepoint(pos_mouse) and estado == "JUGANDO"
                r_draw = rect_op.inflate(6, 4) if hover else rect_op
                r_draw = r_draw.move(ox, oy)
                color_card = (65, 115, 235) if hover else (42, 68, 145)
                pygame.draw.rect(pantalla, color_card, r_draw, border_radius=14)
                pygame.draw.rect(pantalla, (140, 200, 255), r_draw, 2, border_radius=14)

                surf_op = fuente_opcion.render(str(opciones_actuales[i]), True, (255, 255, 255))
                pantalla.blit(surf_op, surf_op.get_rect(center=r_draw.center))

            surf_fb = fuente_sub.render(mensaje_feedback, True, color_feedback)
            pantalla.blit(surf_fb, surf_fb.get_rect(center=(ANCHO // 2 + ox, 532 + oy)))

        else:
            rect_fin = pygame.Rect(120, 170, ANCHO - 240, 310)
            pygame.draw.rect(pantalla, (26, 30, 46), rect_fin, border_radius=18)
            pygame.draw.rect(pantalla, (100, 240, 255) if vidas > 0 else (239, 71, 111), rect_fin, 3, border_radius=18)

            titulo_fin = "🏆 ¡MISIÓN CUMPLIDA!" if vidas > 0 else "💀 ¡SE ACABARON LAS VIDAS!"
            col_fin = (6, 214, 160) if vidas > 0 else (239, 71, 111)
            surf_tfin = fuente_pregunta.render(titulo_fin, True, col_fin)
            pantalla.blit(surf_tfin, surf_tfin.get_rect(center=(ANCHO // 2, 235)))

            sub_fin = "¡Atrapaste a los fantasmas con tus matemáticas!" if vidas > 0 else "Los fantasmas escaparon esta vez. ¡Sigue practicando!"
            surf_sfin = fuente_sub.render(sub_fin, True, (230, 235, 245))
            pantalla.blit(surf_sfin, surf_sfin.get_rect(center=(ANCHO // 2, 295)))

            surf_pfin = fuente_pregunta.render(f"Puntaje Final: {puntos} puntos", True, (255, 215, 100))
            pantalla.blit(surf_pfin, surf_pfin.get_rect(center=(ANCHO // 2, 365)))

            surf_ayuda = fuente_peq.render("Presiona ESPACIO o haz clic en 'Nueva Misión' para jugar otra vez", True, (170, 185, 210))
            pantalla.blit(surf_ayuda, surf_ayuda.get_rect(center=(ANCHO // 2, 435)))

        for rect_b, texto_b, col_b, col_t in (
            (btn_reiniciar, "Nueva Misión (R)", (255, 183, 3), (20, 20, 30)),
            (btn_salir, "Menú (ESC)", (239, 71, 111), (255, 255, 255))
        ):
            hover = rect_b.collidepoint(pos_mouse)
            r_draw = rect_b.inflate(4, 2) if hover else rect_b
            c_bg = tuple(min(255, c + 30) for c in col_b) if hover else col_b
            pygame.draw.rect(pantalla, c_bg, r_draw, border_radius=9)
            t_surf = fuente_sub.render(texto_b, True, col_t)
            pantalla.blit(t_surf, t_surf.get_rect(center=r_draw.center))

        for p in particulas[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vy"] += 0.18
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
