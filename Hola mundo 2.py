#Imprimir & string:
print('hola mundo\nSoy pablo y estoy aprendiendo python')

#Variables y tipos de datos(string incluido):
num_entero = 10
num_real = 99.898
tipo_cadena = 'hola mundo 2'
tipo_bool = True 
print(num_entero)
print(num_real)
print(tipo_cadena)
print(tipo_bool)
resultado_suma = 10+10
print(resultado_suma)

#COMENTARIOS(siempre iniciar con #):

#hola mundo NO tiene mayúscula


#Operadores aritmeticos:
    
sumar = 100+100+100+100+100+100+66
restar = 100-50
multiplicar = 6*100 
dividir = 10000/3
residuo = 10000%3
exponente = 6**6
print(sumar)
print(restar)
print(multiplicar)
print(dividir)
print(residuo)
print(exponente)
dividir = 10000//3
print(dividir)

#Tipos de datos complejos:

#tuplas (datos que una vez colocados NO pueden ser cambiados)
mi_tupla = ('Es mas complejo cada vez, pero me gusta.',2,6,98,3.1,'sip,me gusta.')
print(mi_tupla [0])
print(mi_tupla [1])
print(mi_tupla [2])
print(mi_tupla [3])
print(mi_tupla [4])
print(mi_tupla [5])
print(mi_tupla [0:6])#con esto te ahorras tener que hacer prit'seguidos

#listas(a diferencia de las tuplas, las listas pueden ser modificadas y aunque suene confuso, pueden tener listas dentro de listas)
mi_lista = ['Ejemplo de lista.',24,11,4.0,True,[1,9]]
print(mi_lista[0])
print(mi_lista[1])
print(mi_lista[2])
print(mi_lista[3])
print(mi_lista[4])
print(mi_lista[5])
print(mi_lista[0:6])# a esto se le conocen como rebanadas
	
#modificar datos de listas (se aprecia en la consola de python)
mi_lista[4] = False
print(mi_lista)

#modificar varios datos de la lista (se aprecia en la consola de python)
mi_lista[1:4] = [25,12,'Navidad']
print(mi_lista)

#agregar nuevos items a la lista

mi_lista.append('nuevo ítem')
print(mi_lista)

#funcion len(sirve para enumerar los items de tu lista, también se aprecia en la consola de python)
len(mi_lista)

#comparar listas

lista_uno = [1,2,3]
lista_dos = [4,5,6]
print(lista_uno==lista_dos)#falso

#Diccionarios o matrices asociativas (cada valor tiene asociada una clave, a diferencia de las duplas o de las listas a las cuales se gracias al número de su índice, los diccionarios utilizan una clave para ingresar y declarar un la clave puede ser cualquier tipo de dato inmutable ej:num_entero, num_real,tipo_cadena,tipo_bool,mi_tupla):
 
mi_diccionario = {'clave N°1':1,'clave N°2': 5.0,'clave N°3': 'esto es divertido'}

print(mi_diccionario['clave N°1'])
print(mi_diccionario['clave N°2'])
print(mi_diccionario['clave N°3'])

#también se puede modificar valores como en la lista
mi_diccionario['clave N°1'] = 'Nuevo valor'
print(mi_diccionario['clave N°1'])

#con la función del se pueden eliminar entradas
del(mi_diccionario['clave N°3'])
print(mi_diccionario)# así se puede mostrar el diccionario completo, NO se pueden hacer rebanadas ya que no son secuencias como las listas y tuplas

#Operadores relacionales, se utiliza para hacer comparaciones de cualquier tipo de dato:

print(10==12) #== significa, es = que, se toma como pregunta y en este caso el resultado es falso

print(10==10)#en este caso es verdadero

print(10!=10)#!= significa, es diferente que y en este caso es falso

print(10!=12)#en este caso es verdadero

print(8<9)#< significa, menor que y en este caso es verdadero

print(9<9)#en este caso es falso

print(9>10)#en este caso es falso

print(9>8)#en este caso es verdadero

print(1<=1)#<= significa, menor o igual que y en este caso es verdadero

print(1<=0)#en este caso es falso



#Operadores lógicos, se usa para realizar mas de una comparación:

#and:si una comparación es falsa, el resultado es falso, la única manera de que el resultado sea falso es que ambas sean falsas

#comparaciones falsas
(100>1000) and ('chann'=='chann')

#comparaciones verdaderas 
(1100>1000) and ('chann'=='chann')

#or:mientras una comparación sea verdadera, el resultado será verdadero

#comparaciones verdaderas
(1100<1000)or('chann'=='chann')

#comparaciones falsas
(1100<1000)or('chann'=='PYTHON')

#not:si tu resultado es verdadero lo transforma en falso y si tu resultado es falso lo transforma en verdadero

not (1>0)

not (4<1)

#Control de flujo (if, else,elif) son bloques de código que permiten realizar intrucciones, para que dichas instituciones se puedan ejecutar va a depender de la evolución de una o más condiciones, si esta o estas se cumplen entonces el programa entra en la estructura y ejecuta las instituciones alli puestas, en caso contrario el programa sata está estructura y continuar con su flujo normal:

numero = 1
if numero > 0:
    print('numero es positivo') 

#si la condicion no se cumple

numero = -6
if numero > 0:
    print('numero es positivo')
else:
    print('numero es negativo')

#permite agregar una condición más

numero = 0
if numero > 10:
    print('cruso es real')
elif numero < 5:
    print('curso es fake')
else:
    print('hay que investigar mas')


#Estucturas de control iteraribas, (ciclos o bucles) a diferencia de las condicionales que se ejecutan si si cumplen, en ésta se pueden realizar una o varias iterasiones:

#while:mientras la condicion se cumpla, se ejecutarán las condicionales en una estructura

respuesta = 'si'
numero = 0 
while respuesta =='si':
    numero = int(input('dijite su numero:')) 
if numero > 0: 
  print('El numero ingresado es positivo') 
elif numero < 0:
  print('El numero ingresado es negativo')   
else:
  print('El numero ingresado es igual a 0')
respuesta = input('¿Desea ingresar otro numero? <si - no>') 

#for:nos permite realizar iteraciones sobre una variable compleja ya sea lista o tupla   
mi_lista = ['python','c++','js'] 
for lenguaje in mi_lista:  
    print (lenguaje) 
for edad in range(18,110):
    print('Tu edad es: ', edad)


#Funciones, son bloques de código que realizan una tarea qué devuelve un resultado:

#def:define funciones

def mi_funcion():
    """primera función en python Imprime 2 mensajes"""
    print('hola mundo')
    print('esta es mi primera función en python')

mi_funcion()


#con parámetros
def mi_funcion(cadena, numero):
    """escribe una cadena el número de veces que le asignemos numero"""
    print(cadena * numero)
    mi_funcion('porqueria',666)
    

x = 2

y = 2

res=x*y

res=6

res=x*y