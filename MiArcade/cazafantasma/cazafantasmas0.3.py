import random
import os

# =====================================================================
# 1. EXCEPCIONES PERSONALIZADAS (HERENCIA DE EXCEPTION)
# =====================================================================
class CazafantasmasError(Exception):
    """Excepción base para el juego."""
    pass

class RespuestaVaciaError(CazafantasmasError):
    """Se lanza cuando el jugador no escribe nada e introduce solo un salto de línea."""
    pass

class EnergiaAgotadaError(CazafantasmasError):
    """Se lanza cuando el disparador de protones se queda sin batería."""
    pass

class ValorAbsurdoError(CazafantasmasError):
    """Se lanza si el número introducido supera los límites razonables."""
    pass


# =====================================================================
# 2. FUNCIONES MODULARES Y DE REGLAS DE NEGOCIO
# =====================================================================
def leer_record_historico(archivo: str = "record.txt") -> int:
    """Lee el récord guardado. Si el archivo no existe, maneja FileNotFoundError."""
    manejador = None
    try:
        manejador = open(archivo, "r", encoding="utf-8")
        contenido = manejador.read().strip()
        return int(contenido)
    except FileNotFoundError:
        print("📂 [SISTEMA] No hay récord previo registrado. Creando nueva base de datos...")
        return 0
    except (ValueError, IOError) as err:
        print(f"⚠️ [SISTEMA] Archivo dañado ({err}). Reiniciando récord a 0.")
        return 0
    finally:
        # Aseguramos el cierre manual del recurso si fue abierto
        if manejador is not None:
            manejador.close()

def guardar_record(nuevo_record: int, archivo: str = "record.txt") -> None:
    """Guarda un nuevo récord numérico en el disco."""
    try:
        with open(archivo, "w", encoding="utf-8") as f:
            f.write(str(nuevo_record))
        print("💾 [BITÁCORA] Nuevo récord guardado con éxito.")
    except IOError as e:
        print(f"❌ Error al guardar la bitácora: {e}")

def solicitar_disparo_matematico(prompt: str) -> int:
    """
    Solicita un valor al usuario y realiza validaciones estrictas
    lanzando excepciones estándar y personalizadas con 'raise'.
    """
    entrada = input(prompt).strip()

    # Validación 1: Entrada vacía
    if not entrada:
        raise RespuestaVaciaError("¡El gatillo se atascó! No ingresaste ningún valor.")

    # Validación 2: Tipo de dato entero
    try:
        valor = int(entrada)
    except ValueError:
        raise ValueError("¡Interferencia electromagnética! Solo se admiten números enteros.")

    # Validación 3: Rango de cordura (Regla de negocio)
    if valor < -1000 or valor > 1000:
        raise ValorAbsurdoError("¡Disparo fuera de órbita! El cálculo excede los límites (-1000 a 1000).")

    return valor

def generar_mision(ronda: int) -> tuple[int, int, str, int]:
    """Genera números, operación y calcula el resultado esperado."""
    n1 = random.randint(5, 25)
    n2 = random.randint(1, 10)
    op = random.choice(["+", "-", "*"])

    if op == "+":
        res = n1 + n2
    elif op == "-":
        res = n1 - n2
    else:
        res = n1 * n2

    return n1, n2, op, res


# =====================================================================
# 3. CONTROLADOR PRINCIPAL DEL JUEGO
# =====================================================================
def jugar_cazafantasmas():
    print("🚀 ============================================= 🚀")
    print("   CAZAFANTASMAS 3.0: FRAMEWORK PROFESIONAL       ")
    print("🚀 ============================================= 🚀\n")

    record_actual = leer_record_historico()
    print(f"🏅 Récord histórico a superar: {record_actual} fantasmas.")

    puntos = 0
    energia = 40  # Cada disparo cuesta entre 10 y 15 unidades de energía
    total_rondas = 4

    for ronda in range(1, total_rondas + 1):
        print(f'\n--- Radar Sector #{ronda} | Energía: {energia}% ---')
        n1, n2, op, solucion = generar_mision(ronda)
        print(f'👻 Espectro detectado: ¿Cuánto es {n1} {op} {n2}?')

        try:
            # Comprobación de energía con raise preventivo
            if energia <= 0:
                raise EnergiaAgotadaError("¡El reactor de protones colapsó! Te quedaste sin energía.")

            # Solicitud validada
            disparo = solicitar_disparo_matematico("Ingresa las coordenadas del rayo: ")

        except RespuestaVaciaError as ex_vacia:
            print(f"🟡 ADVERTENCIA: {ex_vacia}")
            energia -= 5
        except ValorAbsurdoError as ex_absurdo:
            print(f"🟠 CALIBRACIÓN ERRÓNEA: {ex_absurdo}")
            energia -= 10
        except ValueError as ex_val:
            print(f"🔴 ERROR CRÍTICO: {ex_val}")
            energia -= 10
        except EnergiaAgotadaError as ex_energia:
            print(f"\n☠️ FIN DE LA MISIÓN: {ex_energia}")
            break  # Detiene la partida de inmediato
        else:
            # Se ejecuta si el input fue un entero válido y no hubo ninguna excepción
            if disparo == solucion:
                print("✨ ¡Captura perfecta! Fantasma asegurado en la trampa.")
                puntos += 1
            else:
                print(f"💨 El rayo rebotó. El fantasma escapó (Solución: {solucion}).")
            energia -= 10
        finally:
            print(f"📊 [Telemetría] Ronda {ronda} finalizada.")

    # Fin de la partida y gestión de récord
    print("\n================ RESULTADOS ================")
    print(f"Puntos obtenidos: {puntos}")
    if puntos > record_actual:
        print("🎉 ¡NUEVO RÉCORD HISTÓRICO ALCANZADO!")
        guardar_record(puntos)
    else:
        print(f"No lograste superar el récord de {record_actual}. ¡Sigue entrenando!")


if __name__ == "__main__":
    jugar_cazafantasmas()