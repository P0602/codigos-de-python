import os
os.system('cls')
respuesta="si"
while (respuesta=="si"):
    delivery1 = 0
    delivery2 = 2000
    delivery3 = 5000
    delivery4 = 10000
    
    #hipoclorito
    hipoclorito_Litro1 = "hipoclorito,1 Litro = $9500"
    hipoclorito_Litro2 = "hipoclorito,2 Litros = $19000"
    hipoclorito_Litro3 = "hipoclorito,3 Litros = $28500"
    
    print("--hipoclorito--")
    print("1.-",hipoclorito_Litro1)
    print("2.-",hipoclorito_Litro2)
    print("3.-",hipoclorito_Litro3)
    opcion = int(input("- Ingrese opción:"))
    if (opcion==1):
        preciohipoclorito = 9500
        detalleshipoclorito = hipoclorito_Litro1
    if (opcion==2):
        preciohipoclorito = 19000
        detalleshipoclorito = hipoclorito_Litro2
    if (opcion==3):
        preciohipoclorito = 28500
        detalleshipoclorito = hipoclorito_Litro3
    
        
    
    #mascarillas
    mascarilla_1 = "Genero simple lavable = $2000"
    mascarilla_2 = "Rígida = $6000"
    
    print("--mascarillas--")
    print("1.-",mascarilla_1)
    print("2.-",mascarilla_2)
    
    opcion = int(input("- Ingrese opción:"))
    if (opcion==1):
        preciomascarilla = 2000
        detallesmascarilla = mascarilla_1
    if (opcion==2):
        preciomascarilla = 6000
        detallesmascarilla = mascarilla_2
    
       
    #desinfectante
    desinfectante1 = "480cm3 = $2500"
    desinfectante2 = "600cm3 = $3100"
    print("--desinfectante--")
    print("1.-",desinfectante1)
    print("2.-",desinfectante2)
    opcion = int(input("- Ingrese opción:"))
    if (opcion==1):
        preciodesinfectante = 2500
        detallesdesinfectante = desinfectante1
    if (opcion==2):
        preciodesinfectante = 3100
        detallesdesinfectante = desinfectante2
    
    print("--- Detalle de Venta ---")
    
    print("hipoclorito:",detalleshipoclorito)
    print("mascarillas:",detallesmascarilla)
    print("desinfectante:",detallesdesinfectante)
    print("delivery > 25.000:$",delivery1)
    print("delivery Santiago Centro:$",delivery2)
    print("delivery providencia,Independencia, Ñuñoa,Estación Central,Independencia",delivery3)
    print("delivery otra comuna:$",delivery4)
      
    #precio 
    total = preciohipoclorito + preciomascarilla + preciodesinfectante
    
    print("Su envió será:$",total)
    
 
    
    respuesta=input("Desea realizar una nueva compra si o no ?:")
    while(respuesta=="si" and respuesta=="no"):
        respuesta=input("Incorrecto ...Desea realizar una nueva compra si o no ?:")

       
print("fin del programa")