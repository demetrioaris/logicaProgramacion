from piedra_papel_y_tijera import piedra_papel_y_tijera
from cazafantasma import cazafantasmas
from ahorcado import ahorcado

def mostrar_menu():
    while True:
        print("=======================================")
        print(" 🕹️  ARCADE VIRTUAL - MENÚ PRINCIPAL  🕹️")
        print("=======================================")
        print("[1] Jugar: Piedra, Papel o Tijera")
        print("[2] Jugar: Cazafantasmas Matemático")
        print("[3] Jugar: Ahorcado")
        print("[4] Salir")
        print("=======================================")
        
        opcion = input("Elige a qué quieres jugar (1-4): ")

        if opcion == "1":
            print("\nAbriendo la carpeta del juego 1...")
            piedra_papel_y_tijera.jugar() 
            
        elif opcion == "2":
            print("\nAbriendo la carpeta del juego 2...")
            cazafantasmas.jugar()

        elif opcion == "3":
            print("\nAbriendo la carpeta del juego 3...")
            ahorcado.jugar()
            
        elif opcion == "4":
            print("\n¡Gracias por jugar! Apagando consola... 📺")
            break
            
        else:
            print("\n❌ Opción no válida.\n")

if __name__ == "__main__":
    mostrar_menu()

    mostrar_menu()