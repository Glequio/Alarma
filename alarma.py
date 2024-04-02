from machine import Pin
import time
import os
import filemod

# Define los pines para filas y columnas del teclado
filas = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT), Pin(5, Pin.OUT)]

columnas = [Pin(6, Pin.IN, Pin.PULL_DOWN), Pin(7, Pin.IN, Pin.PULL_DOWN), Pin(8, Pin.IN, Pin.PULL_DOWN), Pin(9, Pin.IN, Pin.PULL_DOWN)]

# Define las teclas del teclado
teclas = [
    ['1', '2', '3', 'A'],
    ['4', '5', '6', 'B'],
    ['7', '8', '9', 'C'],
    ['*', '0', '#', 'D']
]

keyDigit = 0
NUSER = 5
flag = 0B00000000

#	VALORES DE FLAG
# 00000001 ALARMA ACTIVADA
#
#


# Creo archivos
#os.mkdir("datos")
os.chdir('/')
os.chdir("datos")
# file = open("user.dat","w")
# # pas = open("password.dat","w")
# file.write("GERMAN    \n")	
# file.write("EMILIA    \n")
# file.write("SEBASTIAN \n")
# file.write("USER5     \n")
# file.write("USER6     \n")
# file.write("USER7     \n")
# pas.write("segunda linea\n")
# print(pas.readline())
#file.close()
# 
# os.listdir()

# Función para leer el teclado
def leerTeclado():
    
    for i in range(len(filas)):
        # Configura una columna como salida alta
        filas[i].value(1)
        
        # Lee las filas
        for j in range(len(columnas)):
            if columnas[j].value():
                while(columnas[j].value()):
                    #"aca puede ir el timer de boton pulsado largo"
                    pass
                filas[i].value(0)
                print(teclas[i][j])
                return teclas[i][j]
        filas[i].value(0)
    return 
            
# Funcion clave esta funcion analiza el numero ingresado y lo deriva
# al sector correspondiente

def clave(numero):
    i = 1
    global flag
    print(flag)
    while(i <= NUSER):
        if numero == str(filemod.readline('password.dat',i)):
            usuario = str(filemod.readline('user.dat',i))
            if flag != 0B00000001:
                flag = 0B00000001
                print(usuario," INICIO SISTEMA")
                his = open('history.dat','a')
                his.write(usuario)
                his.write(" Inicio el sistema \n")
                his.close()
                print(flag)
                return
            elif flag == 0B00000001:
                flag = 0B00000000
                print(usuario," DESACTIVO SISTEMA")
                his = open('history.dat','a')
                his.write(usuario)
                his.write(" sistema apagado \n")
                his.close()
                return

        i += 1
    return 
        
 
 
while True:
    
    keyPress = leerTeclado()
    if keyPress:
        if keyDigit == 0:
            numImput = str(keyPress)
            keyDigit += 1
        else:
            numImput += str(keyPress)
            print(numImput)
            if keyDigit == 3:
                print("La clave ingresada es : ",numImput)  
                clave(numImput)
                keyDigit = 0
                numImput = ''

            else:
                keyDigit += 1
     
    time.sleep(0.2)
#     
#     tecla_presionada = leer_teclado()
#     if tecla_presionada:
#         print("Tecla presionada:", tecla_presionada)
#     time.sleep(0.3)  # Espera para evitar la lectura múltiple de una tecla presionada
