import os
os.system('cls')
from datetime import date
#variavles de contador y de selección de números 
contador= 0

FechaCreacion = date(1969,1, 1)#<- inserte fechas aquí ej: año, mes, dia
FechaFinal = date(1970, 1, 1)#<- inserte fechas aquí ej: año, mes, dia
FechasFaltántes = FechaFinal - FechaCreacion

#resultados 
ID = (input("ID:"))
print("Fecha Creacion:", FechaCreacion)
print("Fecha Final:", FechaFinal)
print("Fechas Faltántes en dias:", FechasFaltántes.days)
     
 
print("Fin del programa...")