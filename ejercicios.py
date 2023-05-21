import os

os.system('cls')

estado = True

while estado:

    try:

        nota1 = float(input("Ingrese nota 1:"))

        nota2 = float(input("Ingrese nota 2:"))

        nota3 = float(input("Ingrese nota 3:"))

        if (nota1>=1.0 and nota1<=7.0) and (nota2>=1.0 and nota2<=7.0) and (nota3>=1.0 and nota3<=7.0):

            estado=False

            print(f"Notas son: {nota1}, {nota2}, {nota3}")

            promedio = (nota1+nota2+nota3)/3

            promedio2 = format(promedio,".1f")

            print(f"Promedio es:{promedio2}")

            if promedio>=4.0:

                print("Es aprobado")

            else:

                print("Es reprobado")

        else:

            print("Notas deben ser entre 1 y 7...")

            estado=True

    except:

        print("Notas mal ingresadas...")

print("Fin del programa...")


import os

os.system('cls')

respuesta="si"

while respuesta=="si":

    os.system('cls')

    print("**** TIPO DE TRIANGULO ****")

    ladoA=float(input("Ingrese ladoA: "))

    ladoB=float(input("Ingrese ladoB: "))

    ladoC=float(input("Ingrese ladoC: "))



    if ladoA != ladoB and ladoA != ladoC:

        print("Triangulo es de tipo escaleno")

    elif ladoA == ladoB and ladoA == ladoC:

        print("Triangulo es de tipo equilatero")

    else:

        print("Triangulo es de tipo isosceles")

    respuesta=input("¿ Desea volver a ingresar tipo de triangulo si o no ?")

    while respuesta !="si" and respuesta !="no":

        respuesta=input("Incorrecto!...¿ Desea volver a ingresar tipo de triangulosi o no ?")

print("Fin del programa")

def Sumar(var1, var2):

    resultado = var1 + var2

    return resultado



def Multiplicar():

    valor1 = int(input("Ingrese primer número:"))

    valor2 = int(input("Ingrese segundo número:"))

    resultado = valor1 *  valor2

    print("Multiplicación es:{resultado}")





#Bloque de inicio

import os

os.system('cls')

numero1 = int(input("Ingrese número:"))

numero2 = int(input("Ingrese otro número:"))

sumatoria = Sumar(numero1,numero2)

print(f"Suma es:{sumatoria}")

Multiplicar()

print("Fin del programa...")

