import os
os.system('cls')
print("bienvenido a nuestra tienda online de videojuegos.")
respuesta="si"
while (respuesta=="si"):
    #shooter
    shooter1 = "HALO 5: Guardians, 20 unidades restantes, 1 x $35000"
    shooter2 = "Killzone colletion edition, 30 unidades restantes, 1 x $29990"
    shooter3 = "call of duty: modern warfare, 6 unidades restantes, 1 x $25000"
    shooter4 = "THE WALKING DEAD Survival Instint, 22 unidades restantes, 1 x $20000"
    print("--shooter--")
    print("1.-",shooter1)
    print("2.-",shooter2)
    print("3.-",shooter3)
    print("4.-",shooter4)
    opcion = int(input("- Ingrese opción:"))
    if (opcion==1):
        precioshooter = 35000
        detallesshooter = shooter1
    if (opcion==2):
        precioshooter = 29990
        detallesshooter = shooter2
    if (opcion==3):
        precioshooter = 25000
        detallesshooter = shooter3
    if (opcion==4):
        precioshooter = 20000
        detallesshooter = shooter4
        
    
    #RPG
    RPG1 = "GUNNM: Memorias de Marte(ps1), 30 unidades restantes, 1 x $25000"
    RPG2 = "FINAL FANTASI VII REMAKE, 40 unidades restantes, 1 x $29000"
    RPG3 = "VAGRANT STORY(ps1), 10 unidades restantes, 1 x $25000"
    RPG4 = "ALUNDRA(ps1), 22 unidades restantes, 1 x $20000"
    
    print("--RPG--")
    print("1.-",RPG1)
    print("2.-",RPG2)
    print("3.-",RPG3)
    print("4.-",RPG4)
    opcion = int(input("- Ingrese opción:"))
    if (opcion==1):
        precioRPG = 25000
        detallesRPG = RPG1
    if (opcion==2):
        precioRPG = 29000
        detallesRPG = RPG2
    if (opcion==3):
        precioRPG = 25000
        detallesRPG = RPG3
    if (opcion==4):
        precioRPG = 20000
        detallesRPG = RPG4
       
    #survivalhorror
    survivalhorror1 = "Resident evil clasic colection(ps1), 5 unidades restantes, 1 x $40000"
    survivalhorror2 = "Resident evil REMAKE colection, 10 unidades restantes, 1 x $60000"
    survivalhorror3 = "DINO CRISIS(ps1), 10 unidades restantes, 1 x $25000"
    survivalhorror4 = "Parasite Eve(ps1), 22 unidades restantes, 1 x $20000"
    survivalhorror5 = "Fear Effect(ps1), 22 unidades restantes, 1 x $14000"
    print("--survivalhorror--")
    print("1.-",survivalhorror1)
    print("2.-",survivalhorror2)
    print("3.-",survivalhorror3)
    print("4.-",survivalhorror4)
    print("5.-",survivalhorror5)
    opcion = int(input("- Ingrese opción:"))
    if (opcion==1):
        preciosurvivalhorror = 40000
        detallessurvivalhorror = survivalhorror1
    if (opcion==2):
        preciosurvivalhorror = 60000
        detallessurvivalhorror = survivalhorror2
    if (opcion==3):
        preciosurvivalhorror = 25000
        detallessurvivalhorror = survivalhorror3
    if (opcion==4):
        preciosurvivalhorror = 20000
        detallessurvivalhorror = survivalhorror4
    if (opcion==5):
        preciosurvivalhorror = 14000
        detallessurvivalhorror = survivalhorror5
        
    
    
   
    total = precioshooter + precioRPG + preciosurvivalhorror
    print("total:$",total)
    respuesta=input("Desea realizar una nueva compra si o no ?:")
    while(respuesta=="si" and respuesta=="no"):
        respuesta=input("Incorrecto ...Desea realizar una nueva compra si o no ?:")

       
print("fin del programa")