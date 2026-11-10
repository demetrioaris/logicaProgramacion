import os

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def preguntar_reintentar(mensaje="¿Quieres jugar otra vez?"):
    while True:
        try:
            respuesta = input(f"\n{mensaje} (s/n): ").lower().strip()
            if respuesta not in ["s", "si", "sí", "n", "no"]:
                raise ValueError("Opción no válida. Debes escribir 's' o 'n'.")
            return respuesta in ["s", "si", "sí"]
        except ValueError as error:
            print(f"❌ {error}")

