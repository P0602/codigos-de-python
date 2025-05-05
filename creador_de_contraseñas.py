import random
import string

def generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ""

    # Se agregan los tipos de caracteres según lo que el usuario seleccione
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Debes seleccionar al menos un tipo de caracter."

    # Se genera la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

print("=== Generador de Contraseñas Seguras ===")

try:
    longitud = int(input("Longitud de la contraseña: "))
    mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
    minus = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
    nums = input("¿Incluir números? (s/n): ").lower() == "s"
    simb = input("¿Incluir símbolos? (s/n): ").lower() == "s"

    resultado = generar_contraseña(longitud, mayus, minus, nums, simb)
    print("\nContraseña generada:")
    print(resultado)
except ValueError:
    print("Por favor, ingresa un número válido para la longitud.")import random
import string

def generar_contraseña(longitud, usar_mayusculas, usar_minusculas, usar_numeros, usar_simbolos):
    caracteres = ""

    # Se agregan los tipos de caracteres según lo que el usuario seleccione
    if usar_mayusculas:
        caracteres += string.ascii_uppercase
    if usar_minusculas:
        caracteres += string.ascii_lowercase
    if usar_numeros:
        caracteres += string.digits
    if usar_simbolos:
        caracteres += string.punctuation

    if not caracteres:
        return "Debes seleccionar al menos un tipo de caracter."

    # Se genera la contraseña aleatoria
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

print("=== Generador de Contraseñas Seguras ===")

try:
    longitud = int(input("Longitud de la contraseña: "))
    mayus = input("¿Incluir mayúsculas? (s/n): ").lower() == "s"
    minus = input("¿Incluir minúsculas? (s/n): ").lower() == "s"
    nums = input("¿Incluir números? (s/n): ").lower() == "s"
    simb = input("¿Incluir símbolos? (s/n): ").lower() == "s"

    resultado = generar_contraseña(longitud, mayus, minus, nums, simb)
    print("\nContraseña generada:")
    print(resultado)
except ValueError:
    print("Por favor, ingresa un número válido para la longitud.")