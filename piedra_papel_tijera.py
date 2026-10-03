# Torneo de "Piedra, Papel o Tijera" con Registro de Historial
# Módulos 1-3 - Python fundamentos
# Conceptos: operadores lógicos (and/or), condicionales, listas (.append()),
# len(), iteración con bucles for.
 
import random
 
opciones = ["piedra", "papel", "tijera"]
historial = []
 
num_rondas = int(input("¿Cuántas rondas querés jugar? "))
 
for ronda in range(1, num_rondas + 1):
    print(f"\n--- Ronda {ronda} ---")
    jugador = input("Elegí piedra, papel o tijera: ").lower()
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