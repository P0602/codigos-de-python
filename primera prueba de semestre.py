#Enunciado 1
print("Solución enunciado 1") 
#variavles antes del bucle
contador = 0
#Inicio del bucle
respuesta="si"
while (respuesta=="si"):
    validar = True
    while  (validar):
#Seleccion 
        try:
#seleccion dona
            dona = "Dona = $1200"

            print("----Dona----")
            print (dona)
            cantidad_donas = int(input("¿cuantas Donas deseas comprar?:"))
            precio_dona = 1200
            total_dona = precio_dona*cantidad_donas
            if(cantidad_donas != contador):
                 validar = False
    
#seleccion biscocho
                 Biscocho = "Biscocho = $1500"

                 print("----Biscocho----")
                 print (Biscocho)
                 cantidad_Biscocho = int(input("¿cuantos Biscochos deseas comprar?:"))
                 precio_Biscocho = 1500
                 total_Biscocho = precio_Biscocho*cantidad_Biscocho
            if(cantidad_Biscocho != contador):
                      validar = False
    
#seleccion chileno
                      Chileno = "Chileno = $1000"

                      print("----Chileno----")
                      print (Chileno)
                      cantidad_Chileno = int(input("¿cuantos Chilenos deseas comprar?:"))
                      precio_Chileno = 1000
                      total_Chileno = precio_Chileno*cantidad_Chileno
            if(cantidad_Chileno != contador):
                          validar = False
                          respuesta = input("Desea volver a ingresar si o no:")
        except:
            print("solo se permiten números, intente de nuevo por favor:")
#Fin del bucle
import os 
os.system('cls') 

#Total

print("-------------------------------")
print("Dona\as = $",total_dona)
print("Biscocho\os = $",total_Biscocho)
print("Chileno\os = $",total_Chileno)
print("-------------------------------")
total = total_dona+total_Biscocho+total_Chileno
print("Total:$",total)

#Enunciado 2
print("Solución enunciado 2")
#Inicio del primer bucle
respuesta="si"
while (respuesta=="si"):

    contador = 0
    
    letra1_patente = input("Ingrese primera letra de su patente:")
    letra2_patente = input("Ingrese segunda letra de su patente:")
    letra3_patente = input("Ingrese tercera letra de su patente:")
    letra4_patente = input("Ingrese cuarta letra de su patente:")
    numero1_patente = int(input("Ingrese 1er numero de su patente:"))
    numero2_patente = int(input("Ingrese 2do numero de su patente:"))
    patente_L = letra1_patente, letra2_patente, letra3_patente, letra4_patente
    patente_N = numero1_patente, numero2_patente
    patente = patente_L, patente_N

    letra = input("ingrese letra:")
#Inicio del segundo bucle
    for i in range(5):
        if i == 1:
            if letra == letra1_patente:
                contador = contador + 1
        
        if i == 2:
            if letra == letra2_patente:
                contador = contador + 1
           
        if i == 3:
            if letra == letra3_patente:
                contador = contador + 1
         
        if i == 4:
            if letra == letra4_patente:
                contador = contador + 1
#Fin del bucle  
#Resultado      
    print("En tu patente se repiten",contador,"Vez/veces la letra",letra)
    respuesta=input("Desea realizar una nueva compra si o no ?:")

#Enunciado 3
print("Solución enunciado 3")
#variavles antes del bucle
espacio_vacio = "         "
dato_valido = False

#Inicio del bucle
while not dato_valido:
    try:
        altura = int(input("Ingrese la altura del rectángulo: "))
        if altura > 0 :
            dato_valido = True
        else:
            print("Error: Ingrese un número entero mayor que cero")
    except:
        print("Error: Ingrese un número entero mayor que cero")
    print(" _____________________")
for i in range(altura +0):
    
    print("|",espacio_vacio,espacio_vacio,"|")
print(" _____________________")

#Fin del bucle
