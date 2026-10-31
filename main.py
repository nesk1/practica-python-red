


#Declaracion de variables
opcion = 50
opciones_validas = [0,1,2,3]



#Menu de opciones
while opcion != 0:

    print("1. Comprobar equipos con ping")
    print("2. Guardar MAC de los adaptadores")
    print("3. Ver configuracion de un adaptador")
    print("0. Salir del programa")


    opcion = int(input("Elige una opcion:"))

    if opcion == 1:
      print("Has elegido la Opcion 1")

    if opcion == 2:
         print("Has elegido la Opcion 2")

    if opcion == 3:
            print("Has elegido la Opcion 3")
   
    if opcion not in  opciones_validas:
      print("Opcion incorrecta")




#Funciones

def leer_ip():
    ip = input("Introduce la IP del equipo a comprobar: ")
    return ip
    



    