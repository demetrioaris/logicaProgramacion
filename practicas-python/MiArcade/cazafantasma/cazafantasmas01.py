import random


    print("\n👻 ¡Bienvenido a Cazafantasmas Matemático!")
    # ... (Aquí va todo el código del Nivel 1 o Nivel 2) ...
    print("👻 ============================================ 👻")
    print("   ¡CAZAFANTASMAS MATEMÁTICO 1.0: MODO PRIMARIA!  ")
    print("👻 ============================================ 👻")
    print("¡Ayuda a atrapar a los fantasmas resolviendo sus cuentas!\n")

    puntos = 0
    rondas = 5

    for ronda in range(1, rondas + 1):
        operacion = random.choice(["+", "-", "*", "/"])

        # 1. GENERACIÓN DE NÚMEROS ADAPTADOS A PRIMARIA
        if operacion == "+":
            num1 = random.randint(1, 20)
            num2 = random.randint(1, 20)
            resultado_correcto = num1 + num2

        elif operacion == "-":
            num1 = random.randint(5, 20)
            num2 = random.randint(1, num1)  # Garantiza que el resultado nunca sea negativo
            resultado_correcto = num1 - num2

        elif operacion == "*":
            num1 = random.randint(1, 10)  # Tablas del 1 al 10
            num2 = random.randint(1, 10)
            resultado_correcto = num1 * num2

        else:  # operacion == "/"
            # Técnica inversa: creamos cociente y divisor para asegurar división exacta
            num2 = random.randint(1, 10)               # Divisor (nunca será 0)
            resultado_correcto = random.randint(1, 10) # Cociente esperado
            num1 = num2 * resultado_correcto           # Dividendo exacto

        # 2. PRESENTAR LA PREGUNTA
        simbolo = "÷" if operacion == "/" else ("x" if operacion == "*" else operacion)
        print(f"\n--- Fantasma #{ronda} ---")
        print(f"¿Cuánto es {num1} {simbolo} {num2}?")

        # ⚠️ PUNTO VULNERABLE: Si el niño presiona Enter o escribe letras, el juego colapsa aquí
        respuesta = int(input("Tu respuesta: "))

        # 3. EVALUACIÓN DIRECTA
        if respuesta == resultado_correcto:
            print("⭐ ¡Genial! ¡Atrapaste al fantasma!")
            puntos += 1
        else:
            print(f"💨 ¡Casi! El fantasma escapó. La respuesta era {resultado_correcto}.")

    print("\n==============================================")
    print(f"🏆 Fin del juego: Atrapaste {puntos} de {rondas} fantasmas.")
    print("==============================================")

    print("Fin de la cacería.\n")

if __name__ == "__main__":
    jugar()