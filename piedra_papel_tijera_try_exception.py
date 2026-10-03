
import random
# Si tienes otras librerías, van aquí arriba

def jugar():
    # TODO EL CÓDIGO DEL JUEGO VA AQUÍ ADENTRO (Indentado)
    print("¡Bienvenido a Piedra, Papel o Tijera!")
    
    # Aquí va la lógica de tu juego, los try, except, whiles, etc.
    # ...
    # ...

    # Torneo de "Piedra, Papel o Tijera" con Registro de Historial
    # Módulos 1-4 - Python fundamentos
    # Conceptos: operadores lógicos (and/or), condicionales, listas (.append()),
    # len(), iteración con bucles for, manejo de errores con try/except.

    opciones = ["piedra", "papel", "tijera"]
    historial = []

    # Validamos la cantidad de rondas con try/except: si no es un número válido,
    # se lo volvemos a pedir en vez de romper el programa.
    while True:
        try:
            num_rondas = int(input("¿Cuántas rondas querés jugar? "))
            if num_rondas <= 0:
                print("⚠️ Ingresá un número mayor a cero.")
                continue
            break
        except ValueError:
            print("⚠️ Eso no es un número válido. Probá de nuevo.")

    for ronda in range(1, num_rondas + 1):
        print(f"\n--- Ronda {ronda} ---")

        # Validamos la jugada del jugador: si no es una opción válida,
        # se la volvemos a pedir sin que cuente como una ronda perdida.
        while True:
            try:
                jugador = input("Elegí piedra, papel o tijera: ").lower()
                if jugador not in opciones:
                    raise ValueError("Esa no es una opción válida")
                break
            except ValueError as error:
                print(f"⚠️ {error}. Elegí piedra, papel o tijera.")

        cpu = random.choice(opciones)
        print(f"La computadora eligió: {cpu}")

        if jugador == cpu:
            resultado = "Empate"
        elif (jugador == "piedra" and cpu == "tijera") or \
            (jugador == "papel" and cpu == "piedra") or \
            (jugador == "tijera" and cpu == "papel"):
            resultado = "Victoria"
        else:
            resultado = "Derrota"

        print(f"Resultado: {resultado}")
        historial.append(resultado)

    # Resumen final: recorrer el historial con un for
    print("\n=== Historial del torneo ===")
    for i, resultado in enumerate(historial, start=1):
        print(f"Ronda {i}: {resultado}")

    # Extensión opcional: contar victorias/derrotas/empates
    victorias = historial.count("Victoria")
    derrotas = historial.count("Derrota")
    empates = historial.count("Empate")

    print(f"\nJugaste {len(historial)} rondas.")
    print(f"Victorias: {victorias} | Derrotas: {derrotas} | Empates: {empates}")
        
    print("Fin del juego de Piedra, Papel o Tijera")

# ==========================================
# EL CANDADO DE SEGURIDAD (Esto va al final del archivo, sin indentar)
# ==========================================
if __name__ == "__main__":
    jugar()