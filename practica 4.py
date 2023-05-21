import os
os.system('cls')
respuesta="si"
while (respuesta=="si"):
    códigoing = input(    "Ingese código:")
    tiposalaing = input("ingrese tipo de sala 2D,3D:")
    while (tiposalaing !="2D" and tiposalaing!="3D"):
        tiposalaing = input("Incorrecto. Vuelva a ingresar tipo de sala 2D o 3D:")
    
    cantidading = int(input("ingrese cantidad de entradas:"))
    tipodescuentoing = input("Ingrese tipo descuento cupomatic o ngrupon:")
    
    while(tipodescuentoing !="cupomatic" and tipodescuentoing!="ngrupon"):
        tipodescuentoing = input("Incorrecto. Vuelva a ingresar descuento cupomatic o ngrupon:")
    if (tiposalaing=="2D"):
        precio = 4000
    else:
        precio = 4600
        
    subtotal = precio * cantidading
    if (tipodescuentoing=="ngrupon"):
        total = subtotal - (subtotal*0.10)
    elif (tipodescuentoing=="cupomatic"):
        total = subtotal - (subtotal*0.15)

    print("-- Comprobante de Descuento con Cupón --")
    print("Código película:",códigoing)
    print("Tipo sala:",tiposalaing)
    print("Cupón:",tipodescuentoing)
    print("Cantidad de entradas:",cantidading)
    print("Precio unitario:$",precio)
    print("subtotal:$",subtotal)
    print("Total con descuento:$",total)
    respuesta = input("Desea volver a ingresar si o no:")
    while (respuesta!="si" and respuesta!="no"):
        respuesta = input("Incorrecto.Desea volver a ingresar si o no:")
