# Esta funcion modifica datos especificos cargados uno debajo de otro
# Parametros:
#		Nombre de archivo
# 		Longitud de datos
# 		Numero de linea que queremos modificar o borrar
# 		Nuevo valor


import os

def filemod(archivo,ldata,nline,newvalor):
    file = open(archivo)
    listaFile = file.readlines()
    if ldata < len(newvalor)+1 :
        print("Longitud de nuevo valor excede maximo")
        return
    listaFile[nline-1] = newvalor + '\n'
    file = open(archivo,'w')
    for i in range(len(listaFile)):
        file.write(listaFile[i])
    file.close()
    print("correccion terminada")
    return

def clearline(archivo,ldata):
    file = open(archivo)
    listaFile = file.readlines()        
    file = open(archivo,'w')
    for i in range(len(listaFile)):
        if i+1 != ldata :
            file.write(listaFile[i])
    file.close()
    return

def insline(archivo,ldata,nline,newvalor):
    file = open(archivo)
    listaFile = file.readlines()
    if ldata < len(newvalor)+1 :
        print("Longitud de nuevo valor excede maximo")
        return
#    listaFile[nline-1] = newvalor + '\n'
    file = open(archivo,'w')
    for i in range(len(listaFile)):
        if i+1 == nline:
            file.write(newvalor + '\n')
        file.write(listaFile[i])
    file.close()
    print("correccion terminada")
    return

def readline(archivo,ldata):
    file = open(archivo)
    listaFile = file.readlines()        
    return listaFile[ldata-1]

def datazize(archivo):
    file = open(archivo)
    listaFile = file.readlines()
    return len(listaFile)

def dataprint(archivo,lstar,lend):	# Si lstar = lend = 0 me imprime todo el archivo
    file = open(archivo)
    listaFile = file.readlines()
    print("CANTIDAD TOTALES DE DATOS: ",len(listaFile))
    if lstar == 0 and lend == 0:	#se imprime todo
        for i in range(len(listaFile)):
            print("DATO ",i+1,": ",listaFile[i])
        return
        
    else:
        i = lstar-1
        while(i < lend):
            print("DATO ",i+1,": ",listaFile[i])
            i += 1
            
    file.close()
    
    
os.chdir("prueba")
# file = open("archivo.dat","a")
# for i in range(1000):
#     file.write("1234567890\n")
# file.close()
# filemod('archivo.dat',11,3,'nuñvf 7890')
# #clearline('archivo.dat',3)
# insline('archivo.dat',11,2,'222vf 7890')
# print(readline('archivo.dat',2))