import random
import string

def generar_contraseña(longitud, usar_mayus, usar_minus, usar_nums, usar_simbolos):
    caracteres = ""

    if usar_mayus:
        caracteres += string.ascii_uppercase
    if usar_minus:
        caracteres += string.ascii_lowercase
    if usar_nums:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        print("Debes seleccionar al menos un tipo de carácter.")
        return None

    # Generar la contraseña
    contraseña = ''.join(random.choices(caracteres, k=longitud))
    return contraseña

def preguntar_si(texto):
    while True:
        respuesta = input(texto + " (s/n): ").lower()
        if respuesta in ['s', 'n']:
            return respuesta == 's'
        else:
            print("Por favor responde solo con 's' o 'n'.")

if __name__ == "__main__":
    print("=== Generador de Contraseñas Personalizado ===\n")

    try:
        nombre = input("¿Cuál es tu nombre? ")
        print(f"\n¡Hola {nombre}!, vamos a crear una contraseña segura para ti.\n")

        longitud = int(input("¿Qué longitud deseas para tu contraseña? (mínimo 6): "))
        if longitud < 6:
            print("La longitud mínima es de 6 caracteres.")
        else:
            usar_mayus = preguntar_si("¿Quieres incluir MAYÚSCULAS?")
            usar_minus = preguntar_si("¿Quieres incluir minúsculas?")
            usar_nums = preguntar_si("¿Quieres incluir números?")
            usar_simbolos = preguntar_si("¿Quieres incluir símbolos (como @, #, $)?")

            print("\nGenerando tu contraseña segura...\n")
            contraseña = generar_contraseña(longitud, usar_mayus, usar_minus, usar_nums, usar_simbolos)

            if contraseña:
                print(f"{nombre}, tu nueva contraseña es:")
                print(contraseña)
    except ValueError:
        print("Debes ingresar un número válido para la longitud.")