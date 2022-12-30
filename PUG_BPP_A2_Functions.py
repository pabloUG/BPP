import os
import io

def crearFichero (nombre):
    
    creado = False
    
    if os.path.isfile(nombre):
        file = open(nombre,"a")
        creado = True
    else:
        file = open(nombre,"w")
        creado = True 
        
    file.close()
    
    return creado

def suma(a,b=0):
    return (a + b)

def deleteFile(nombre):
    
    if os.path.isfile(nombre):
        os.remove(nombre)
        borrado = True
    else:
        borrado = False
        
    return borrado


    
