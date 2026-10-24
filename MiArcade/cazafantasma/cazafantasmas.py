import random

def jugar():
    print("⚡ ============================================ ⚡")
    print("   ¡CAZAFANTASMAS 2.0: ESCUDO ECTOPLÁSMICO!      ")
    print("   (Juego protegido con try - except - else - finally) ")
    print("⚡ ============================================ ⚡\n")

    trampas = {
        "red": 10,
        "aspiradora": 20,
        "laser": 30
    }

    puntos_totales = 0
    bateria = 100
    rondas = 3

    for ronda in range(1, rondas + 1):
        print(f"\n================ Ronda {ronda} de {rondas} ================")

        trampa_activa = None
        while trampa_activa is None:
            print(f"🎒 Mochila de artefactos: {list(trampas.keys())}")
            eleccion = input("Elige tu trampa: ").strip().lower()

            try:
                puntos_premio = trampas[eleccion]
                trampa_activa = eleccion
                print(f"👉 Equipaste: ¡{trampa_activa.capitalize()}! Vale {puntos_premio} puntos.")
            except KeyError:
                print(f"⚠️ ¡Ese artefacto no está en la mochila! Prueba con: {list(trampas.keys())}")

        op = random.choice(["+", "-", "*", "/"])
        if op == "+":
            n1 = random.randint(1, 20)
            n2 = random.randint(1, 20)
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
        print(f"\n👻 Aparece un fantasma: ¿Cuánto es {n1} {simbolo} {n2}?")

        try:
            disparo = int(input("Escribe el resultado con los números del teclado: "))
        except ValueError:
            print("🛡️ [ESCUDO ACTIVO] ¡Eso no fue un número! El rayo se dispersó de forma segura.")
        else:
            if disparo == solucion:
                print(f"🎉 ¡Excelente disparo! Atrapaste al fantasma con la {trampa_activa}.")
                puntos_totales += puntos_premio
            else:
                print(f"💨 ¡Estuvo cerca! El fantasma se escondió. La respuesta era {solucion}.")
        finally:
            bateria -= 20
            print(f"🔋 [SISTEMA] Enfriando trampa... Batería restante: {bateria}%")

    print("\n==============================================")
    print("🏁 ¡Misión terminada!")
    print(f"Puntaje final: {puntos_totales} puntos | Batería restante: {bateria}%.")
    print("==============================================")

if __name__ == "__main__":
    jugar()
