import os
import random

def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

def jugar():
    while True:
        vidas = 3
        puntos = 0
        ronda = 1
        total_rondas = 5
        mensaje = ""

        while ronda <= total_rondas and vidas > 0:
            limpiar_pantalla()

            print("⚡ ============================================ ⚡")
            print("        👻 CAZAFANTASMAS MATEMÁTICO 👻           ")
            print("⚡ ============================================ ⚡")
            corazones = "❤️ " * vidas
            print(f"Vidas: {corazones.strip()} | Puntos: {puntos} | Fantasma: {ronda} de {total_rondas}")
            print("=" * 48)

            if mensaje:
                print(f"\n{mensaje}\n" + "-" * 48)

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
            print(f"\n👻 ¡Aparece un fantasma! Resuelve:")
            print(f"👉 ¿Cuánto es {n1} {simbolo} {n2}?")

            try:
                disparo = int(input("\n🔢 Tu disparo: ").strip())
            except ValueError:
                mensaje = "🛡️ [ESCUDO] ¡Escribe solo números con el teclado!"
            else:
                if disparo == solucion:
                    puntos += 10
                    mensaje = "🎉 ¡ZAP! ¡Excelente disparo, atrapaste al fantasma! (+10 puntos)"
                else:
                    vidas -= 1
                    mensaje = f"💨 ¡El fantasma escapó! La respuesta correcta era {solucion}."
                ronda += 1

        limpiar_pantalla()
        print("⚡ ============================================ ⚡")
        print("        👻 CAZAFANTASMAS MATEMÁTICO 👻           ")
        print("⚡ ============================================ ⚡\n")

        if vidas > 0:
            print("🏆 ¡MISIÓN CUMPLIDA! Lograste atrapar a los fantasmas.")
        else:
            print("💀 ¡Te quedaste sin vidas! Los fantasmas escaparon.")

        print(f"\n⭐ Puntaje final: {puntos} puntos")
        print("=" * 48)

        while True:
            try:
                repetir = input("\n¿Quieres jugar otra vez? (s/n): ").lower().strip()
                if repetir not in ["s", "si", "sí", "n", "no"]:
                    raise ValueError("Opción no válida. Debes escribir 's' o 'n'.")

                if repetir in ["s", "si", "sí"]:
                    break
                else:
                    return
            except ValueError as error:
                print(f"❌ {error}")

if __name__ == "__main__":
    jugar()
