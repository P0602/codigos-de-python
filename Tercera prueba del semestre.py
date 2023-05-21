# Escribir	 un	 programa	 que	 permita	 al	 usuario	 crear	 una	 lista	 con	 nombres,	 estos	 deben	 ser
# ingresados	 por	 el	 usuario	 hasta	 que	 indique	 que	 no	 desea	 ingresar	más. Luego	 el	 programa
# debe	 solicitar	ingresar	 un	 nombre	y	 buscarlo	en	la	lista,	mostrando	 como	 resultado	 si	existe
# dentro	de	ésta	y	cuantas	veces.

patentes = []

continuar = True
while continuar:
    patente = input("Ingrese patente: ")
    patentes.append(patente)

    


letra = input("Ingrese una letra de la patente: ").lower()
veces = 0

for patente in patentes:
    if letra == patente.lower():
        veces = veces + 1

print(f"El nombre {busqueda} se encontró {veces} veces en la lista")
