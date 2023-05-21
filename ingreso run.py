import os
os.system('cls')
respuesta="si"
while (respuesta=="si"):
    try:
        run = int(input("ingrese su run:"))
    except:
        print("Por favor ingrese un run de 10 caracteres y con guion")          