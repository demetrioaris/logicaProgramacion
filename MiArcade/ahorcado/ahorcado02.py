
import os
import random
import string
from MiArcade.ahorcado.hangman_visual import lives_visual_dict
from MiArcade.ahorcado.palabras import palabras  # Lista de palabras

def limpiar_pantalla():
    """Limpia la terminal adaptándose al sistema operativo (Windows o Linux/macOS)."""
    os.system('cls' if os.name == 'nt' else 'clear')

def obtener_palabra_valida(palabras):
    """Selecciona una palabra aleatoria sin espacios ni guiones."""
    palabra = random.choice(palabras)
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)
    return palabra.upper()

def seleccionar_dificultad():
    """Permite al usuario elegir la dificultad usando try/except para validar la opción."""
    while True:
        limpiar_pantalla()
        print("==========================================")
        print("   🎮 BIENVENIDO AL JUEGO DEL AHORCADO 🎮   ")
        print("==========================================")
        print("\n--- SELECCIONA EL NIVEL DE DIFICULTAD ---")
        print("1. Fácil (9 vidas)")
        print("2. Medio (6 vidas)")
        print("3. Difícil (4 vidas)")

        try:
            opcion = int(input("\nIngresa el número de tu opción (1, 2 o 3): "))
            if opcion == 1:
                return 9, "Fácil"
            elif opcion == 2:
                return 6, "Medio"
            elif opcion == 3:
                return 4, "Difícil"
            else:
                input("\n❌ Opción fuera de rango. Presiona Enter para intentar de nuevo...")
        except ValueError:
            input("\n❌ Entrada no válida. Presiona Enter para ingresar un número (1, 2 o 3)...")

def jugar_partida(vidas_iniciales, nivel):
    """Ejecuta una partida completa del juego del Ahorcado."""
    palabra = obtener_palabra_valida(palabras)
    letras_palabra = set(palabra)
    abecedario = set(string.ascii_uppercase)
    letras_usadas = set()
    vidas = vidas_iniciales
    mensaje = ""  # Mensaje para mostrar al usuario tras cada intento

    while len(letras_palabra) > 0 and vidas > 0:
        limpiar_pantalla()
        
        print(f"Modo: nivel | Vidas restantes: {vidas}")
        
        # Mostramos las letras usadas o 'Ninguna' si la lista está vacía
        letras_texto = ", ".join(sorted(letras_usadas)) if letras_usadas else "Ninguna"
        print(f"Letras usadas: {letras_texto}\n")

        # Visualización de la figura ASCII y la palabra oculta
        if vidas in lives_visual_dict:
            print(lives_visual_dict[vidas])

        lista_palabra = [letra if letra in letras_usadas else '-' for letra in palabra]
        print("\nPalabra actual:", " ".join(lista_palabra))

        # Muestra mensajes de estado anteriores (acierto, error o advertencia)
        if mensaje:
            print(f"\n{mensaje}")
            mensaje = ""

        # Lectura de la entrada del usuario protegida con try / except
        try:
            letra_usuario = input("\nAdivina una letra: ").upper().strip()

            if len(letra_usuario) != 1:
                raise ValueError("Debes ingresar exactamente una sola letra.")

            if not letra_usuario.isalpha():
                raise ValueError("Solo se permiten letras del abecedario (sin números ni símbolos).")

        except ValueError as error:
            mensaje = f"❌ Error de entrada: {error}"
            continue

        # Procesar la letra válida
        if letra_usuario in abecedario - letras_usadas:
            letras_usadas.add(letra_usuario)

            if letra_usuario in letras_palabra:
                letras_palabra.remove(letra_usuario)
                mensaje = "✨ ¡Bien hecho! La letra está en la palabra."
            else:
                vidas -= 1
                mensaje = f"❌ La letra '{letra_usuario}' no está en la palabra."

        elif letra_usuario in letras_usadas:
            mensaje = "⚠️ Ya habías probado esa letra. Intenta con otra."

    # Resultado final de la partida
    limpiar_pantalla()
    if vidas == 0:
        if vidas in lives_visual_dict:
            print(lives_visual_dict[vidas])
        print(f"\n☠️ ¡Lo siento, te quedaste sin vidas! La palabra era: {palabra}")
        return False
    else:
        print(f"\n🎉 ¡GENIAL! Adivinaste la palabra: {palabra}")
        return True

def juego_ahorcado():
    """Controlador principal del juego con contador de victorias y partidas."""
    victorias = 0
    partidas_jugadas = 0

    while True:
        partidas_jugadas += 1
        vidas_iniciales, nivel = seleccionar_dificultad()

        gano = jugar_partida(vidas_iniciales, nivel)
        if gano:
            victorias += 1

        # Resumen de estadísticas
        print("\n------------------------------------------")
        print(f"📊 MARCADOR: {victorias} victoria(s) en {partidas_jugadas} partida(s).")
        print("------------------------------------------")

        # Confirmación para volver a jugar
        while True:
            respuesta = input("\n¿Quieres jugar otra partida? (S/N): ").strip().upper()
            if respuesta in ['S', 'N']:
                break
            print("❌ Respuesta no válida. Escribe 'S' para Sí o 'N' para No.")

        if respuesta == 'N':
            limpiar_pantalla()
            print("==========================================")
            print("      ¡GRACIAS POR JUGAR AL AHORCADO! 👋  ")
            print(f"      Puntaje Final: {victorias}/{partidas_jugadas} victorias.  ")
            print("==========================================")
            break

if __name__ == '__main__':
    juego_ahorcado()
