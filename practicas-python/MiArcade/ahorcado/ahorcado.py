
import random
import string
from MiArcade.ahorcado.hangman_visual import lives_visual_dict
from MiArcade.ahorcado.palabras import palabras  # Lista de palabras

def obtener_palabra_valida(palabras):
    palabra = random.choice(palabras)  # Elige aleatoriamente una palabra de la lista
    
    # Se evitan palabras con guiones o espacios para simplificar el juego
    while '-' in palabra or ' ' in palabra:
        palabra = random.choice(palabras)

    return palabra.upper()

def ahorcado():
    palabra = obtener_palabra_valida(palabras)
    letras_palabra = set(palabra)  # Conjunto de letras únicas en la palabra a adivinar
    abecedario = set(string.ascii_uppercase)  # Conjunto de letras del abecedario en mayúsculas
    letras_usadas = set()  # Conjunto de letras que el usuario ya ha intentado

    vidas = 7

    # Bucle principal: se ejecuta mientras queden letras por adivinar y le queden vidas al jugador
    while len(letras_palabra) > 0 and vidas > 0:
        # Muestra las vidas restantes y las letras que ya se han usado
        print('Te quedan', vidas, 'vidas y has usado estas letras: ', ' '.join(letras_usadas))

        # Muestra el estado actual de la palabra (ejemplo: P - L A B R A)
        lista_palabra = [letra if letra in letras_usadas else '-' for letra in palabra]
        print(lives_visual_dict[vidas])
        print('Palabra actual: ', ' '.join(lista_palabra))

        # Solicita una letra al usuario y la convierte a mayúscula
        letra_usuario = input('Adivina una letra: ').upper()

        # Verifica si es una letra válida del abecedario que aún no se ha usado
        if letra_usuario in abecedario - letras_usadas:
            letras_usadas.add(letra_usuario)
            
            if letra_usuario in letras_palabra:
                letras_palabra.remove(letra_usuario)
                print('')

            else:
                vidas = vidas - 1  # Resta una vida si la letra no está en la palabra
                print('\nLa letra', letra_usuario, 'no está en la palabra.')

        elif letra_usuario in letras_usadas:
            print('\nYa has usado esa letra. Intenta con otra.')

        else:
            print('\nEsa no es una letra válida.')

    # El juego termina cuando se adivinan todas las letras O cuando las vidas llegan a 0
    if vidas == 0:
        print(lives_visual_dict[vidas])
        print('Perdiste, lo siento. La palabra era:', palabra)
    else:
        print('¡GENIAL! ¡Adivinaste la palabra', palabra, '!')

if __name__ == '__main__':
    ahorcado()