import pygame
import random
import math
import array

def crear_sonido(frecuencia, duracion_ms, volumen=0.22):
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

def jugar():
    pygame.init()
    try:
        pygame.mixer.init(frequency=44100, size=-16, channels=1)
    except Exception:
        pass

    snd_comer = crear_sonido(680, 110, 0.25)
    snd_choque = crear_sonido(150, 320, 0.3)
    snd_click = crear_sonido(520, 70, 0.2)

    ANCHO, ALTO = 760, 660
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("La Serpiente (Snake) - MiArcade (60 FPS)")
    reloj = pygame.time.Clock()

    CELDA = 24
    COLS = 28
    FILAS = 22
    TABLERO_ANCHO = COLS * CELDA
    TABLERO_ALTO = FILAS * CELDA
    OFFSET_X = (ANCHO - TABLERO_ANCHO) // 2
    OFFSET_Y = 96

    fuente_titulo = pygame.font.SysFont("Arial Black", 32, bold=True)
    fuente_sub = pygame.font.SysFont("Arial", 18, bold=True)
    fuente_grande = pygame.font.SysFont("Arial Black", 24, bold=True)
    fuente_peq = pygame.font.SysFont("Arial", 14, bold=True)

    dificultades = {
        "Fácil": 115,
        "Normal": 78,
        "Difícil": 48
    }
    dificultad_actual = "Normal"
    intervalo_ms = dificultades[dificultad_actual]

    temas_color = [
        {"nombre": "Verde Clásico", "cabeza": (50, 255, 100), "cuerpo": (28, 175, 70)},
        {"nombre": "Azul Neón", "cabeza": (77, 243, 255), "cuerpo": (30, 144, 255)},
        {"nombre": "Fuego", "cabeza": (255, 215, 60), "cuerpo": (255, 110, 30)},
        {"nombre": "Morado Mágico", "cabeza": (235, 100, 255), "cuerpo": (145, 50, 200)}
    ]
    indice_color = 0

    estado_juego = "MENU"
    puntos = 0
    record = 0

    cabeza = [COLS // 2, FILAS // 2]
    cuerpo = []
    direccion = (0, 0)
    cola_direcciones = []
    comida = [5, 5]

    ultimo_movimiento = 0
    shake_frames = 0
    particulas = []

    btn_menu_jugar = pygame.Rect(ANCHO // 2 - 150, 240, 300, 52)
    btn_menu_opciones = pygame.Rect(ANCHO // 2 - 150, 310, 300, 52)
    btn_menu_salir = pygame.Rect(ANCHO // 2 - 150, 380, 300, 52)

    btn_dif_1 = pygame.Rect(170, 235, 130, 46)
    btn_dif_2 = pygame.Rect(315, 235, 130, 46)
    btn_dif_3 = pygame.Rect(460, 235, 130, 46)
    btn_cambiar_color = pygame.Rect(ANCHO // 2 - 140, 390, 280, 48)
    btn_volver_menu = pygame.Rect(ANCHO // 2 - 140, 490, 280, 48)

    def colocar_comida():
        nonlocal comida
        while True:
            cx = random.randint(0, COLS - 1)
            cy = random.randint(0, FILAS - 1)
            if [cx, cy] != cabeza and [cx, cy] not in cuerpo:
                comida = [cx, cy]
                break

    def lanzar_particulas(px, py, color):
        for _ in range(28):
            ang = random.uniform(0, 2 * math.pi)
            vel = random.uniform(1.5, 6.0)
            particulas.append({
                "x": float(px),
                "y": float(py),
                "vx": math.cos(ang) * vel,
                "vy": math.sin(ang) * vel,
                "radio": random.randint(3, 6),
                "color": color,
                "vida": random.randint(20, 40)
            })

    def iniciar_partida():
        nonlocal estado_juego, puntos, cabeza, cuerpo, direccion, ultimo_movimiento
        estado_juego = "JUGANDO"
        puntos = 0
        cabeza = [COLS // 2, FILAS // 2]
        cuerpo = [[COLS // 2 - 1, FILAS // 2], [COLS // 2 - 2, FILAS // 2]]
        direccion = (0, 0)
        cola_direcciones.clear()
        particulas.clear()
        colocar_comida()
        ultimo_movimiento = pygame.time.get_ticks()

    def registrar_direccion(nueva_dir):
        nonlocal direccion
        if estado_juego != "JUGANDO":
            return

        ref_dir = cola_direcciones[-1] if cola_direcciones else direccion

        if direccion == (0, 0):
            if nueva_dir == (-1, 0):
                return
            direccion = nueva_dir
            cola_direcciones.clear()
            return

        opuesto = (-ref_dir[0], -ref_dir[1])
        if nueva_dir != ref_dir and nueva_dir != opuesto:
            if len(cola_direcciones) < 2:
                cola_direcciones.append(nueva_dir)

    def paso_serpiente():
        nonlocal puntos, record, estado_juego, direccion, shake_frames

        if direccion == (0, 0):
            return

        if cola_direcciones:
            direccion = cola_direcciones.pop(0)

        nueva_cabeza = [cabeza[0] + direccion[0], cabeza[1] + direccion[1]]

        if (nueva_cabeza[0] < 0 or nueva_cabeza[0] >= COLS or
                nueva_cabeza[1] < 0 or nueva_cabeza[1] >= FILAS or
                nueva_cabeza in cuerpo):
            if puntos > record:
                record = puntos
            estado_juego = "GAMEOVER"
            shake_frames = 14
            reproducir(snd_choque)
            return

        cuerpo.insert(0, [cabeza[0], cabeza[1]])
        cabeza[0], cabeza[1] = nueva_cabeza[0], nueva_cabeza[1]

        if cabeza == comida:
            puntos += 1
            if puntos > record:
                record = puntos
            reproducir(snd_comer)
            px = OFFSET_X + comida[0] * CELDA + CELDA // 2
            py = OFFSET_Y + comida[1] * CELDA + CELDA // 2
            lanzar_particulas(px, py, (255, 80, 95))
            colocar_comida()
        else:
            cuerpo.pop()

    def dibujar_boton(rect, texto, color_base, pos_mouse, color_texto=(255, 255, 255)):
        hover = rect.collidepoint(pos_mouse)
        r_draw = rect.inflate(6, 4) if hover else rect
        c_bg = tuple(min(255, c + 30) for c in color_base) if hover else color_base
        pygame.draw.rect(pantalla, c_bg, r_draw, border_radius=12)
        pygame.draw.rect(pantalla, (255, 255, 255), r_draw, 2, border_radius=12)
        surf = fuente_sub.render(texto, True, color_texto)
        pantalla.blit(surf, surf.get_rect(center=r_draw.center))

    ejecutando = True
    while ejecutando:
        ahora = pygame.time.get_ticks()
        pos_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_UP, pygame.K_w):
                    registrar_direccion((0, -1))
                elif evento.key in (pygame.K_DOWN, pygame.K_s):
                    registrar_direccion((0, 1))
                elif evento.key in (pygame.K_LEFT, pygame.K_a):
                    registrar_direccion((-1, 0))
                elif evento.key in (pygame.K_RIGHT, pygame.K_d):
                    registrar_direccion((1, 0))
                elif evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                    if estado_juego in ("MENU", "GAMEOVER"):
                        reproducir(snd_click)
                        iniciar_partida()
                elif evento.key == pygame.K_p:
                    if estado_juego == "JUGANDO":
                        estado_juego = "PAUSA"
                    elif estado_juego == "PAUSA":
                        estado_juego = "JUGANDO"
                        ultimo_movimiento = ahora
                elif evento.key == pygame.K_o:
                    if estado_juego in ("MENU", "GAMEOVER"):
                        reproducir(snd_click)
                        estado_juego = "OPCIONES"
                elif evento.key == pygame.K_m:
                    if estado_juego in ("OPCIONES", "PAUSA", "GAMEOVER"):
                        reproducir(snd_click)
                        estado_juego = "MENU"
                elif evento.key == pygame.K_ESCAPE:
                    if estado_juego in ("OPCIONES", "PAUSA", "GAMEOVER"):
                        reproducir(snd_click)
                        estado_juego = "MENU"
                    elif estado_juego == "JUGANDO":
                        estado_juego = "PAUSA"
                    else:
                        ejecutando = False
                elif estado_juego == "OPCIONES":
                    if evento.key in (pygame.K_1, pygame.K_KP1):
                        dificultad_actual = "Fácil"
                        intervalo_ms = dificultades["Fácil"]
                        reproducir(snd_click)
                    elif evento.key in (pygame.K_2, pygame.K_KP2):
                        dificultad_actual = "Normal"
                        intervalo_ms = dificultades["Normal"]
                        reproducir(snd_click)
                    elif evento.key in (pygame.K_3, pygame.K_KP3):
                        dificultad_actual = "Difícil"
                        intervalo_ms = dificultades["Difícil"]
                        reproducir(snd_click)
                    elif evento.key == pygame.K_c:
                        indice_color = (indice_color + 1) % len(temas_color)
                        reproducir(snd_click)

            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if estado_juego == "MENU":
                    if btn_menu_jugar.collidepoint(pos_mouse):
                        reproducir(snd_click)
                        iniciar_partida()
                    elif btn_menu_opciones.collidepoint(pos_mouse):
                        reproducir(snd_click)
                        estado_juego = "OPCIONES"
                    elif btn_menu_salir.collidepoint(pos_mouse):
                        reproducir(snd_click)
                        ejecutando = False
                elif estado_juego == "OPCIONES":
                    if btn_dif_1.collidepoint(pos_mouse):
                        dificultad_actual = "Fácil"
                        intervalo_ms = dificultades["Fácil"]
                        reproducir(snd_click)
                    elif btn_dif_2.collidepoint(pos_mouse):
                        dificultad_actual = "Normal"
                        intervalo_ms = dificultades["Normal"]
                        reproducir(snd_click)
                    elif btn_dif_3.collidepoint(pos_mouse):
                        dificultad_actual = "Difícil"
                        intervalo_ms = dificultades["Difícil"]
                        reproducir(snd_click)
                    elif btn_cambiar_color.collidepoint(pos_mouse):
                        indice_color = (indice_color + 1) % len(temas_color)
                        reproducir(snd_click)
                    elif btn_volver_menu.collidepoint(pos_mouse):
                        reproducir(snd_click)
                        estado_juego = "MENU"
                elif estado_juego == "GAMEOVER":
                    if btn_menu_jugar.collidepoint(pos_mouse):
                        reproducir(snd_click)
                        iniciar_partida()
                    elif btn_menu_opciones.collidepoint(pos_mouse):
                        reproducir(snd_click)
                        estado_juego = "OPCIONES"
                    elif btn_menu_salir.collidepoint(pos_mouse):
                        reproducir(snd_click)
                        estado_juego = "MENU"

        if estado_juego == "JUGANDO" and ahora - ultimo_movimiento >= intervalo_ms:
            ultimo_movimiento = ahora
            paso_serpiente()

        ox, oy = 0, 0
        if shake_frames > 0:
            shake_frames -= 1
            ox = random.randint(-5, 5)
            oy = random.randint(-5, 5)

        pantalla.fill((14, 16, 24))

        rect_hud = pygame.Rect(OFFSET_X + ox, 22 + oy, TABLERO_ANCHO, 54)
        pygame.draw.rect(pantalla, (24, 28, 42), rect_hud, border_radius=12)
        pygame.draw.rect(pantalla, (55, 65, 95), rect_hud, 2, border_radius=12)

        texto_hud = f"Puntos: {puntos}        |        Récord: {record}        |        Nivel: {dificultad_actual}"
        surf_hud = fuente_sub.render(texto_hud, True, (240, 245, 255))
        pantalla.blit(surf_hud, surf_hud.get_rect(center=rect_hud.center))

        for fila in range(FILAS):
            for col in range(COLS):
                color_celda = (20, 24, 36) if (fila + col) % 2 == 0 else (24, 29, 44)
                rect_c = pygame.Rect(OFFSET_X + col * CELDA + ox, OFFSET_Y + fila * CELDA + oy, CELDA, CELDA)
                pygame.draw.rect(pantalla, color_celda, rect_c)

        rect_borde = pygame.Rect(OFFSET_X - 3 + ox, OFFSET_Y - 3 + oy, TABLERO_ANCHO + 6, TABLERO_ALTO + 6)
        pygame.draw.rect(pantalla, temas_color[indice_color]["cabeza"], rect_borde, 3, border_radius=6)

        if estado_juego in ("JUGANDO", "PAUSA", "GAMEOVER"):
            pulso = int(math.sin(ahora * 0.01) * 2)
            cx_com = OFFSET_X + comida[0] * CELDA + CELDA // 2 + ox
            cy_com = OFFSET_Y + comida[1] * CELDA + CELDA // 2 + oy
            pygame.draw.circle(pantalla, (255, 55, 80), (cx_com, cy_com), CELDA // 2 - 2 + pulso)
            pygame.draw.circle(pantalla, (255, 180, 190), (cx_com - 3, cy_com - 3), 3)
            pygame.draw.line(pantalla, (80, 220, 100), (cx_com, cy_com - 8), (cx_com + 4, cy_com - 13), 3)

            color_cuerpo = temas_color[indice_color]["cuerpo"]
            for seg in cuerpo:
                r_seg = pygame.Rect(OFFSET_X + seg[0] * CELDA + 2 + ox, OFFSET_Y + seg[1] * CELDA + 2 + oy, CELDA - 4, CELDA - 4)
                pygame.draw.rect(pantalla, color_cuerpo, r_seg, border_radius=6)

            color_cabeza = temas_color[indice_color]["cabeza"]
            r_cab = pygame.Rect(OFFSET_X + cabeza[0] * CELDA + 1 + ox, OFFSET_Y + cabeza[1] * CELDA + 1 + oy, CELDA - 2, CELDA - 2)
            pygame.draw.rect(pantalla, color_cabeza, r_cab, border_radius=7)

            ojo1 = (r_cab.centerx - 4, r_cab.centery - 4)
            ojo2 = (r_cab.centerx + 4, r_cab.centery - 4)
            pygame.draw.circle(pantalla, (15, 18, 28), ojo1, 3)
            pygame.draw.circle(pantalla, (15, 18, 28), ojo2, 3)

            if direccion == (0, 0) and estado_juego == "JUGANDO":
                surf_aviso = fuente_sub.render("Presiona una Flecha o W/A/S/D para empezar a moverte", True, (255, 215, 100))
                pantalla.blit(surf_aviso, surf_aviso.get_rect(center=(ANCHO // 2, OFFSET_Y + TABLERO_ALTO - 30)))

        for p in particulas[:]:
            p["x"] += p["vx"]
            p["y"] += p["vy"]
            p["vida"] -= 1
            if p["vida"] <= 0:
                particulas.remove(p)
            else:
                pygame.draw.circle(pantalla, p["color"], (int(p["x"]), int(p["y"])), p["radio"])

        if estado_juego != "JUGANDO":
            overlay = pygame.Surface((TABLERO_ANCHO, TABLERO_ALTO), pygame.SRCALPHA)
            overlay.fill((12, 14, 22, 215))
            pantalla.blit(overlay, (OFFSET_X, OFFSET_Y))

        if estado_juego == "MENU":
            surf_t = fuente_titulo.render("S N A K E   G A M E", True, temas_color[indice_color]["cabeza"])
            pantalla.blit(surf_t, surf_t.get_rect(center=(ANCHO // 2, 175)))

            dibujar_boton(btn_menu_jugar, "Comenzar a Jugar (ESPACIO)", (6, 180, 125), pos_mouse)
            dibujar_boton(btn_menu_opciones, "Opciones y Color (O)", (58, 134, 255), pos_mouse)
            dibujar_boton(btn_menu_salir, "Volver al Arcade (ESC)", (239, 71, 111), pos_mouse)

            surf_ctrl = fuente_peq.render("Controles: Flechas o W/A/S/D para moverte  |  P para Pausa", True, (170, 185, 210))
            pantalla.blit(surf_ctrl, surf_ctrl.get_rect(center=(ANCHO // 2, 575)))

        elif estado_juego == "OPCIONES":
            surf_op = fuente_grande.render("OPCIONES Y PERSONALIZACIÓN", True, (255, 209, 102))
            pantalla.blit(surf_op, surf_op.get_rect(center=(ANCHO // 2, 165)))

            surf_d = fuente_sub.render("1. Selecciona la Velocidad (Teclas 1, 2, 3):", True, (230, 235, 245))
            pantalla.blit(surf_d, surf_d.get_rect(center=(ANCHO // 2, 210)))

            for rect_d, nom_d in ((btn_dif_1, "Fácil"), (btn_dif_2, "Normal"), (btn_dif_3, "Difícil")):
                activo = (dificultad_actual == nom_d)
                col_d = (6, 214, 160) if activo else (45, 55, 80)
                col_txt = (15, 18, 28) if activo else (230, 235, 245)
                dibujar_boton(rect_d, nom_d, col_d, pos_mouse, col_txt)

            surf_c = fuente_sub.render(f"2. Tema de la Serpiente: {temas_color[indice_color]['nombre']}", True, temas_color[indice_color]["cabeza"])
            pantalla.blit(surf_c, surf_c.get_rect(center=(ANCHO // 2, 355)))

            dibujar_boton(btn_cambiar_color, "🎨 Cambiar Color (C)", temas_color[indice_color]["cuerpo"], pos_mouse)
            dibujar_boton(btn_volver_menu, "⬅ Guardar y Volver (M)", (75, 85, 120), pos_mouse)

        elif estado_juego == "PAUSA":
            surf_p = fuente_titulo.render("JUEGO EN PAUSA", True, (255, 209, 102))
            pantalla.blit(surf_p, surf_p.get_rect(center=(ANCHO // 2, 280)))

            surf_pi = fuente_sub.render("Presiona [ P ] para continuar o [ M ] para volver al menú", True, (240, 245, 255))
            pantalla.blit(surf_pi, surf_pi.get_rect(center=(ANCHO // 2, 350)))

        elif estado_juego == "GAMEOVER":
            surf_go = fuente_titulo.render("¡ G A M E   O V E R !", True, (239, 71, 111))
            pantalla.blit(surf_go, surf_go.get_rect(center=(ANCHO // 2, 165)))

            surf_pts = fuente_sub.render(f"Puntuación final: {puntos}   |   Récord: {record}", True, (255, 215, 100))
            pantalla.blit(surf_pts, surf_pts.get_rect(center=(ANCHO // 2, 210)))

            dibujar_boton(btn_menu_jugar, "🔄 Reintentar (ESPACIO)", (6, 180, 125), pos_mouse)
            dibujar_boton(btn_menu_opciones, "⚙️ Opciones (O)", (58, 134, 255), pos_mouse)
            dibujar_boton(btn_menu_salir, "⬅ Menú de Snake (M)", (100, 110, 140), pos_mouse)

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()

if __name__ == "__main__":
    jugar()
