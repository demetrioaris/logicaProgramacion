import pygame
import random
import math
import array

from piedra_papel_y_tijera import piedra_papel_y_tijera
from cazafantasma import cazafantasmas
from ahorcado import ahorcado
from serpiente import juego_serpiente

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

def dibujar_icono_juego(superficie, id_juego, cx, cy, color_acento, tiempo_ms):
    onda = int(math.sin(tiempo_ms * 0.005 + id_juego) * 4)
    cy_anim = cy + onda

    pygame.draw.circle(superficie, (20, 24, 38), (cx, cy_anim), 38)
    pygame.draw.circle(superficie, color_acento, (cx, cy_anim), 38, 3)

    if id_juego == 1:
        pygame.draw.line(superficie, (230, 235, 245), (cx - 12, cy_anim + 10), (cx + 14, cy_anim - 16), 4)
        pygame.draw.line(superficie, (230, 235, 245), (cx + 12, cy_anim + 10), (cx - 14, cy_anim - 16), 4)
        pygame.draw.circle(superficie, color_acento, (cx - 14, cy_anim + 14), 8, 3)
        pygame.draw.circle(superficie, color_acento, (cx + 14, cy_anim + 14), 8, 3)

    elif id_juego == 2:
        pygame.draw.circle(superficie, color_acento, (cx, cy_anim - 6), 18)
        pygame.draw.rect(superficie, color_acento, (cx - 18, cy_anim - 6, 36, 20))
        for i in range(3):
            px = cx - 18 + i * 12
            pygame.draw.polygon(superficie, color_acento, [(px, cy_anim + 14), (px + 12, cy_anim + 14), (px + 6, cy_anim + 22)])
        pygame.draw.circle(superficie, (255, 255, 255), (cx - 6, cy_anim - 6), 5)
        pygame.draw.circle(superficie, (255, 255, 255), (cx + 6, cy_anim - 6), 5)
        pygame.draw.circle(superficie, (20, 24, 38), (cx - 5, cy_anim - 6), 2)
        pygame.draw.circle(superficie, (20, 24, 38), (cx + 7, cy_anim - 6), 2)

    elif id_juego == 3:
        pygame.draw.line(superficie, color_acento, (cx - 16, cy_anim + 18), (cx + 16, cy_anim + 18), 3)
        pygame.draw.line(superficie, color_acento, (cx - 10, cy_anim + 18), (cx - 10, cy_anim - 18), 3)
        pygame.draw.line(superficie, color_acento, (cx - 10, cy_anim - 18), (cx + 8, cy_anim - 18), 3)
        pygame.draw.line(superficie, color_acento, (cx + 8, cy_anim - 18), (cx + 8, cy_anim - 10), 2)
        pygame.draw.circle(superficie, (240, 245, 255), (cx + 8, cy_anim - 4), 6, 2)
        pygame.draw.line(superficie, (240, 245, 255), (cx + 8, cy_anim + 2), (cx + 8, cy_anim + 12), 2)

    elif id_juego == 4:
        segmentos = [
            (cx - 14, cy_anim + 10),
            (cx - 4, cy_anim + 10),
            (cx - 4, cy_anim),
            (cx + 6, cy_anim),
            (cx + 6, cy_anim - 10)
        ]
        for sx, sy in segmentos[:-1]:
            pygame.draw.rect(superficie, (40, 200, 100), (sx - 5, sy - 5, 10, 10), border_radius=2)
        hx, hy = segmentos[-1]
        pygame.draw.rect(superficie, (120, 255, 140), (hx - 6, hy - 6, 12, 12), border_radius=3)
        pygame.draw.circle(superficie, (255, 70, 90), (cx + 18, cy_anim - 10), 5)

def seleccionar_juego_pygame():
    pygame.init()
    try:
        pygame.mixer.init(frequency=44100, size=-16, channels=1)
    except Exception:
        pass

    snd_hover = crear_sonido(520, 45, 0.12)
    snd_click = crear_sonido(780, 140, 0.25)

    ANCHO, ALTO = 820, 640
    pantalla = pygame.display.set_mode((ANCHO, ALTO))
    pygame.display.set_caption("🕹️ MiArcade - Menú Principal")
    reloj = pygame.time.Clock()

    fuente_titulo = pygame.font.SysFont("Arial Black", 32, bold=True)
    fuente_sub = pygame.font.SysFont("Arial", 16, bold=True)
    fuente_card_titulo = pygame.font.SysFont("Arial Black", 18, bold=True)
    fuente_card_desc = pygame.font.SysFont("Arial", 14)
    fuente_tag = pygame.font.SysFont("Arial", 12, bold=True)

    estrellas = [
        {
            "x": random.uniform(0, ANCHO),
            "y": random.uniform(0, ALTO),
            "vel": random.uniform(0.3, 1.2),
            "radio": random.choice([1, 2])
        }
        for _ in range(65)
    ]

    tarjetas = [
        {
            "id": 1,
            "titulo": "[1] Piedra, Papel o\nTijera",
            "desc": "Duelo clásico con animaciones",
            "tag": "PYGAME 60 FPS",
            "color": (58, 134, 255),
            "rect": pygame.Rect(65, 140, 325, 175)
        },
        {
            "id": 2,
            "titulo": "[2] Cazafantasmas",
            "desc": "Atrapa fantasmas con matemáticas",
            "tag": "PYGAME 60 FPS",
            "color": (6, 214, 160),
            "rect": pygame.Rect(430, 140, 325, 175)
        },
        {
            "id": 3,
            "titulo": "[3] El Ahorcado",
            "desc": "Descubre la palabra con teclado",
            "tag": "PYGAME 60 FPS",
            "color": (255, 183, 3),
            "rect": pygame.Rect(65, 345, 325, 175)
        },
        {
            "id": 4,
            "titulo": "[4] La Serpiente \n(Snake)",
            "desc": "Come manzanas y supera tu récord",
            "tag": "PYGAME 60 FPS",
            "color": (168, 85, 247),
            "rect": pygame.Rect(430, 345, 325, 175)
        }
    ]

    btn_salir = pygame.Rect(295, 555, 230, 48)
    ultimo_hover = None
    eleccion = None

    ejecutando = True
    while ejecutando:
        ahora = pygame.time.get_ticks()
        pos_mouse = pygame.mouse.get_pos()

        for evento in pygame.event.get():
            if evento.type == pygame.QUIT:
                eleccion = 5
                ejecutando = False
            elif evento.type == pygame.KEYDOWN:
                if evento.key in (pygame.K_ESCAPE, pygame.K_5, pygame.K_KP5):
                    eleccion = 5
                    ejecutando = False
                elif evento.key in (pygame.K_1, pygame.K_KP1):
                    reproducir(snd_click)
                    eleccion = 1
                    ejecutando = False
                elif evento.key in (pygame.K_2, pygame.K_KP2):
                    reproducir(snd_click)
                    eleccion = 2
                    ejecutando = False
                elif evento.key in (pygame.K_3, pygame.K_KP3):
                    reproducir(snd_click)
                    eleccion = 3
                    ejecutando = False
                elif evento.key in (pygame.K_4, pygame.K_KP4):
                    reproducir(snd_click)
                    eleccion = 4
                    ejecutando = False
            elif evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1:
                for t in tarjetas:
                    if t["rect"].collidepoint(pos_mouse):
                        reproducir(snd_click)
                        pygame.time.delay(110)
                        eleccion = t["id"]
                        ejecutando = False
                        break
                if btn_salir.collidepoint(pos_mouse):
                    reproducir(snd_click)
                    pygame.time.delay(110)
                    eleccion = 5
                    ejecutando = False

        pantalla.fill((14, 16, 26))

        for est in estrellas:
            est["y"] += est["vel"]
            if est["y"] > ALTO:
                est["y"] = 0
                est["x"] = random.uniform(0, ANCHO)
            pygame.draw.circle(pantalla, (75, 85, 120), (int(est["x"]), int(est["y"])), est["radio"])

        surf_titulo = fuente_titulo.render("ARCADE VIRTUAL - MENÚ PRINCIPAL", True, (77, 243, 255))
        pantalla.blit(surf_titulo, surf_titulo.get_rect(center=(ANCHO // 2, 52)))

        surf_sub = fuente_sub.render("Haz clic en un cartucho para jugar o presiona las teclas [1 - 4]", True, (180, 195, 220))
        pantalla.blit(surf_sub, surf_sub.get_rect(center=(ANCHO // 2, 95)))

        hover_actual = None
        for t in tarjetas:
            es_hover = t["rect"].collidepoint(pos_mouse)
            if es_hover:
                hover_actual = t["id"]

            r_draw = t["rect"].inflate(8, 6) if es_hover else t["rect"]
            color_fondo = (32, 38, 58) if es_hover else (22, 26, 40)
            grosor_borde = 4 if es_hover else 2

            pygame.draw.rect(pantalla, color_fondo, r_draw, border_radius=16)
            pygame.draw.rect(pantalla, t["color"], r_draw, grosor_borde, border_radius=16)

            dibujar_icono_juego(pantalla, t["id"], r_draw.x + 56, r_draw.centery, t["color"], ahora)

            rect_tag = pygame.Rect(r_draw.x + 108, r_draw.y + 22, 130, 22)
            pygame.draw.rect(pantalla, t["color"], rect_tag, border_radius=6)
            surf_tag = fuente_tag.render(t["tag"], True, (15, 18, 28))
            pantalla.blit(surf_tag, surf_tag.get_rect(center=rect_tag.center))

            lineas_titulo = t["titulo"].split("\n")
            y_texto = r_draw.y + 52
            for linea in lineas_titulo:
                surf_t = fuente_card_titulo.render(linea, True, (255, 255, 255))
                pantalla.blit(surf_t, (r_draw.x + 108, y_texto))
                y_texto += 24

            surf_d = fuente_card_desc.render(t["desc"], True, (175, 185, 210))
            pantalla.blit(surf_d, (r_draw.x + 108, y_texto + 8))

            txt_jugar = "JUGAR AHORA" if es_hover else "Clic para abrir"
            col_jugar = t["color"] if es_hover else (110, 120, 145)
            surf_j = fuente_tag.render(txt_jugar, True, col_jugar)
            pantalla.blit(surf_j, (r_draw.x + 108, r_draw.y + 132))

        hover_salir = btn_salir.collidepoint(pos_mouse)
        if hover_salir:
            hover_actual = 5

        if hover_actual is not None and hover_actual != ultimo_hover:
            reproducir(snd_hover)
        ultimo_hover = hover_actual

        r_salir = btn_salir.inflate(6, 4) if hover_salir else btn_salir
        col_salir = (255, 95, 130) if hover_salir else (239, 71, 111)
        pygame.draw.rect(pantalla, col_salir, r_salir, border_radius=12)
        pygame.draw.rect(pantalla, (255, 255, 255), r_salir, 2, border_radius=12)
        surf_salir = fuente_sub.render("Apagar Consola (ESC)", True, (255, 255, 255))
        pantalla.blit(surf_salir, surf_salir.get_rect(center=r_salir.center))

        pygame.display.flip()
        reloj.tick(60)

    pygame.quit()
    return eleccion

def mostrar_menu():
    while True:
        opcion = seleccionar_juego_pygame()

        if opcion == 1:
            piedra_papel_y_tijera.jugar()
        elif opcion == 2:
            cazafantasmas.jugar()
        elif opcion == 3:
            ahorcado.jugar()
        elif opcion == 4:
            juego_serpiente.jugar()
        else:
            print("\n¡Gracias por jugar! Apagando consola...")
            break

if __name__ == "__main__":
    mostrar_menu()
