import pygame
import random
import string
import math
import array

from ahorcado.palabras import palabras

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

def obtener_palabra_valida(lista_palabras):
    reemplazos = str.maketrans("ÁÉÍÓÚáéíóú", "AEIOUaeiou")
    palabra = random.choice(lista_palabras)
    while "-" in palabra or " " in palabra:
        palabra = random.choice(lista_palabras)
    return palabra.translate(reemplazos).upper()

def dibujar_ahorcado(superficie, cx, cy, vidas):
    color_estructura = (140, 155, 185)
    color_cuerda = (255, 209, 102)
    color_personaje = (77, 243, 255) if vidas > 0 else (239, 71, 111)

    pygame.draw.line(superficie, color_estructura, (cx - 75, cy + 105), (cx + 75, cy + 105), 6)

    if vidas <= 6:
        pygame.draw.line(superficie, color_estructura, (cx - 45, cy + 105), (cx - 45, cy - 95), 6)
    if vidas <= 5:
        pygame.draw.line(superficie, color_estructura, (cx - 45, cy - 95), (cx + 25, cy - 95), 6)
        pygame.draw.line(superficie, color_estructura, (cx - 45, cy - 65), (cx - 15, cy - 95), 4)
        pygame.draw.line(superficie, color_cuerda, (cx + 25, cy - 95), (cx + 25, cy - 65), 4)
    if vidas <= 4:
        pygame.draw.circle(superficie, color_personaje, (cx + 25, cy - 45), 20, 4)
        if vidas == 0:
            pygame.draw.line(superficie, color_personaje, (cx + 16, cy - 51), (cx + 22, cy - 45), 2)
            pygame.draw.line(superficie, color_personaje, (cx + 22, cy - 51), (cx + 16, cy - 45), 2)
            pygame.draw.line(superficie, color_personaje, (cx + 28, cy - 51), (cx + 34, cy - 45), 2)
            pygame.draw.line(superficie, color_personaje, (cx + 34, cy - 51), (cx + 28, cy - 45), 2)
    if vidas <= 3:
        pygame.draw.line(superficie, color_personaje, (cx + 25, cy - 25), (cx + 25, cy + 35), 4)
    if vidas <= 2:
        pygame.draw.line(superficie, color_personaje, (cx + 25, cy - 12), (cx - 2, cy + 16), 4)
    if vidas <= 1:
        pygame.draw.line(superficie, color_personaje, (cx + 25, cy - 12), (cx + 52, cy + 16), 4)
    if vidas <= 0:
        pygame.draw.line(superficie, color_personaje, (cx + 25, cy + 35), (cx + 2, cy + 78), 4)
        pygame.draw.line(superficie, color_personaje, (cx + 25, cy + 35), (cx + 48, cy + 78), 4)

def jugar():
    pygame.init()
    try:
        pygame.mixer.init(frequency=44100, size=-16, channels=1)
    except Exception:
        pass

    snd_acierto = crear_sonido(640, 120, 0.25)
    snd_fallo = crear_sonido(190, 220, 0.28)
    snd_alerta = crear_sonido(420, 110, 0.2)
    snd_victoria = crear_sonido(860, 320, 0.3)

    ANCHO, ALTO = 820, 650
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("El Ahorcado - MiArcade (60 FPS)")
    reloj = pygame.time.Clock()

    fuente_titulo = pygame.font.SysFont("Arial Black", 26, bold=True)
    fuente_palabra = pygame.font.SysFont("Consolas", 34, bold=True)
    fuente_sub = pygame.font.SysFont("Arial", 17, bold=True)
    fuente_tecla = pygame.font.SysFont("Arial Black", 18, bold=True)

    abecedario = set(string.ascii_uppercase)

    palabra = ""
    letras_palabra = set()
    letras_usadas = set()
    vidas = 7
    racha_victorias = 0
    estado = "JUGANDO"

    mensaje = "¡Haz clic en una letra o escríbela en tu teclado!"
    color_mensaje = (200, 215, 245)

    shake_frames = 0
    particulas = []

    teclas_virtuales = []
    letras_ordenadas = list(string.ascii_uppercase)
    filas_teclado = [letras_ordenadas[0:9], letras_ordenadas[9:18], letras_ordenadas[18:26]]

    for idx_fila, fila in enumerate(filas_teclado):
        ancho_tecla = 54
        alto_tecla = 46
        espacio = 8
        total_ancho_fila = len(fila) * ancho_tecla + (len(fila) - 1) * espacio
        inicio_x = (ANCHO - total_ancho_fila) // 2
        y_fila = 405 + idx_fila * (alto_tecla + espacio)
        for idx_col, letra in enumerate(fila):
            x_tecla = inicio_x + idx_col * (ancho_tecla + espacio)
            teclas_virtuales.append({
                "letra": letra,
                "rect": pygame.Rect(x_tecla, y_fila, ancho_tecla, alto_tecla)
            })

    btn_nueva = pygame.Rect(215, 582, 185, 44)
    btn_salir = pygame.Rect(420, 582, 185, 44)

    def lanzar_confeti(x, y):
        colores = [(6, 214, 160), (255, 209, 102), (77, 243, 255), (255, 95, 162)]
        for _ in range(55):
            ang = random.uniform(0, 2 * math.pi)
            vel = random.uniform(2.0, 8.0)
            particulas.append({
                "x": float(x),
                "y": float(y),
                "vx": math.cos(ang) * vel,
                "vy": math.sin(ang) * vel - 2.0,
                "radio": random.randint(4, 7),
                "color": random.choice(colores),
                "vida": random.randint(35, 60)
            })

    def iniciar_partida():
        nonlocal palabra, letras_palabra, letras_usadas, vidas, estado, mensaje, color_mensaje
        palabra = obtener_palabra_valida(palabras)
        letras_palabra = set(palabra)
        letras_usadas = set()
        vidas = 7
        estado = "JUGANDO"
        mensaje = "¡Adivina la palabra oculta! Tienes 7 vidas."
        color_mensaje = (200, 215, 245)
        particulas.clear()

    def intentar_letra(letra_usuario):
        nonlocal vidas, estado, mensaje, color_mensaje, shake_frames, racha_victorias

        if estado != "JUGANDO":
            return

        letra_usuario = letra_usuario.upper().strip()

        try:
            if len(letra_usuario) != 1:
                raise ValueError("Debes ingresar exactamente una sola letra.")
            if letra_usuario not in abecedario:
                raise ValueError("Usa únicamente letras del abecedario (A-Z).")
            if letra_usuario in letras_usadas:
                raise ValueError(f"Ya habías intentado la letra '{letra_usuario}'.")

            letras_usadas.add(letra_usuario)

            if letra_usuario in letras_palabra:
                letras_palabra.remove(letra_usuario)
                mensaje = f"✅ ¡Bien! La letra '{letra_usuario}' está en la palabra."
                color_mensaje = (6, 214, 160)
                reproducir(snd_acierto)
            else:
                vidas -= 1
                mensaje = f"❌ La letra '{letra_usuario}' no está en la palabra."
                color_mensaje = (239, 71, 111)
                shake_frames = 12
                reproducir(snd_fallo)

            if len(letras_palabra) == 0:
                estado = "GANADO"
                racha_victorias += 1
                mensaje = f"🎉 ¡GENIAL! Adivinaste la palabra: {palabra}"
                color_mensaje = (6, 214, 160)
                reproducir(snd_victoria)
                lanzar_confeti(ANCHO // 2, 230)
            elif vidas <= 0:
                estado = "PERDIDO"
                racha_victorias = 0
                mensaje = f"💀 ¡Perdiste! La palabra era: {palabra}"
                color_mensaje = (239, 71, 111)

        except ValueError as error:
            mensaje = f"⚠️ {error}"
            color_mensaje = (255, 209, 102)
            reproducir(snd_alerta)

    iniciar_partida()

    ejecutando = True
    while ejecutando:
        pos_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key == pygame.K_ESCAPE:
                    ejecutando = False
                elif estado != "JUGANDO" and evento.key in (pygame.K_SPACE, pygame.K_RETURN):
                    iniciar_partida()
                elif estado == "JUGANDO" and evento.unicode and evento.unicode.isalpha():
                    intentar_letra(evento.unicode)
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                if btn_nueva.collidepoint(pos_mouse):
                    iniciar_partida()
                elif btn_salir.collidepoint(pos_mouse):
                    ejecutando = False
                elif estado == "JUGANDO":
                    for t in teclas_virtuales:
                        if t["rect"].collidepoint(pos_mouse):
                            intentar_letra(t["letra"])
                            break

        ox, oy = 0, 0
        if shake_frames > 0:
            shake_frames -= 1
            ox = random.randint(-5, 5)
            oy = random.randint(-5, 5)

        pantalla.fill((15, 18, 28))

        surf_titulo = fuente_titulo.render("EL AHORCADO - DESAFÍO DE PALABRAS", True, (255, 183, 3))
        pantalla.blit(surf_titulo, surf_titulo.get_rect(center=(ANCHO // 2 + ox, 34 + oy)))

        rect_hud = pygame.Rect(60 + ox, 62 + oy, ANCHO - 120, 44)
        pygame.draw.rect(pantalla, (26, 30, 46), rect_hud, border_radius=10)
        pygame.draw.rect(pantalla, (55, 65, 95), rect_hud, 2, border_radius=10)

        texto_hud = f"Vidas restantes: {vidas} / 7        |        Letras usadas: {len(letras_usadas)}        |        Racha: {racha_victorias}"
        surf_hud = fuente_sub.render(texto_hud, True, (240, 245, 255))
        pantalla.blit(surf_hud, surf_hud.get_rect(center=rect_hud.center))

        rect_panel_dibujo = pygame.Rect(60 + ox, 120 + oy, 230, 225)
        pygame.draw.rect(pantalla, (22, 26, 40), rect_panel_dibujo, border_radius=14)
        pygame.draw.rect(pantalla, (60, 70, 100), rect_panel_dibujo, 2, border_radius=14)
        dibujar_ahorcado(pantalla, rect_panel_dibujo.centerx, rect_panel_dibujo.centery + 5, vidas)

        rect_panel_palabra = pygame.Rect(310 + ox, 120 + oy, 450, 225)
        pygame.draw.rect(pantalla, (22, 26, 40), rect_panel_palabra, border_radius=14)
        pygame.draw.rect(pantalla, (60, 70, 100), rect_panel_palabra, 2, border_radius=14)

        lbl_oculta = fuente_sub.render("PALABRA OCULTA:", True, (150, 165, 195))
        pantalla.blit(lbl_oculta, lbl_oculta.get_rect(center=(rect_panel_palabra.centerx, 165 + oy)))

        lista_mostrar = [letra if (letra in letras_usadas or estado == "PERDIDO") else "_" for letra in palabra]
        texto_palabra = " ".join(lista_mostrar)

        escala_fuente = fuente_palabra
        if len(palabra) > 10:
            escala_fuente = pygame.font.SysFont("Consolas", 26, bold=True)

        color_pal = (6, 214, 160) if estado == "GANADO" else ((239, 71, 111) if estado == "PERDIDO" else (255, 255, 255))
        surf_palabra = escala_fuente.render(texto_palabra, True, color_pal)
        pantalla.blit(surf_palabra, surf_palabra.get_rect(center=(rect_panel_palabra.centerx, 235 + oy)))

        if estado != "JUGANDO":
            surf_extra = fuente_sub.render("Presiona ESPACIO o 'Nueva Palabra' para jugar otra vez", True, (255, 209, 102))
            pantalla.blit(surf_extra, surf_extra.get_rect(center=(rect_panel_palabra.centerx, 305 + oy)))

        surf_msg = fuente_sub.render(mensaje, True, color_mensaje)
        pantalla.blit(surf_msg, surf_msg.get_rect(center=(ANCHO // 2 + ox, 372 + oy)))

        for t in teclas_virtuales:
            letra_t = t["letra"]
            usada = letra_t in letras_usadas
            acertada = usada and (letra_t in palabra)
            hover = t["rect"].collidepoint(pos_mouse) and not usada and estado == "JUGANDO"

            r_draw = t["rect"].inflate(4, 4) if hover else t["rect"]
            r_draw = r_draw.move(ox, oy)

            if acertada:
                c_bg = (6, 175, 130)
                c_borde = (100, 255, 200)
                c_txt = (255, 255, 255)
            elif usada:
                c_bg = (45, 30, 42)
                c_borde = (120, 55, 75)
                c_txt = (120, 110, 125)
            elif hover:
                c_bg = (65, 115, 235)
                c_borde = (255, 255, 255)
                c_txt = (255, 255, 255)
            else:
                c_bg = (34, 42, 66)
                c_borde = (85, 100, 145)
                c_txt = (230, 235, 245)

            pygame.draw.rect(pantalla, c_bg, r_draw, border_radius=8)
            pygame.draw.rect(pantalla, c_borde, r_draw, 2, border_radius=8)
            surf_l = fuente_tecla.render(letra_t, True, c_txt)
            pantalla.blit(surf_l, surf_l.get_rect(center=r_draw.center))

        for rect_b, texto_b, col_b, col_t in (
            (btn_nueva, "🔄 Nueva Palabra", (255, 183, 3), (20, 20, 30)),
            (btn_salir, "🚪 Menú (ESC)", (239, 71, 111), (255, 255, 255))
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
