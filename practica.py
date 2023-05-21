print('buenos días, me llamo iris y seré su asistente en este registro.')

print('para empezar:')

respuesta="si"
while (respuesta=="si"):

 nombre = input('¿Cuál es tu nombre?:')

 rut = input('¿Cuál es tu rut?:')
 
 correoelectronicoing = input('¿Cuál es su correo electrónico?:')

 claveing = input('registre una clave de su preferencia:')
 
 correoelectronico = input('vuelta a ingresar su correo electrónico:')
 
 clave = input('vuelta a ingresar su clave:')
 
 if (correoelectronico == correoelectronicoing and clave == claveing):
 
  print("Acceso Consedido, hola",nombre)
 
 else:
  print("Acceso Denegado")

 respuesta = input("Ingrese si para repetir, no para salir:")

print("Fin del programa...")