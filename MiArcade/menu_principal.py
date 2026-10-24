# MODO CORRECTO DE USAR RUTAS RELATIVAS EN PYTHON:
# from [nombre_carpeta] import [nombre_archivo]


from piedra_papel_tijeras import piedra_papel_tijera_try_exception
from cazafantasma import cazafantasmas01

def mostrar_menu():
    while True:
        print("=======================================")
        print(" 🕹️  ARCADE VIRTUAL - MENÚ PRINCIPAL  🕹️")
        print("=======================================")
        print("[1] Jugar: Piedra, Papel o Tijera")
        print("[2] Jugar: Cazafantasmas Matemático")
        print("[3] Salir")
        print("=======================================")
        
        opcion = input("Elige a qué quieres jugar (1-3): ")

        if opcion == "1":
            print("\nAbriendo la carpeta del juego 1...")
            # Como ya lo importamos arriba, lo llamamos directo
            piedra_papel_tijera_try_exception.jugar() 
            
        elif opcion == "2":
            print("\nAbriendo la carpeta del juego 2...")
            cazafantasmas01.jugar()
            
        elif opcion == "3":
            print("\n¡Gracias por jugar! Apagando consola... 📺")
            break
            
        else:
            print("\n❌ Opción no válida.\n")

if __name__ == "__main__":
    mostrar_menu()