class MyException(Exception):
    pass

class NumerUpTen(MyException):
    pass      
    

def MyFuntion():
    
    try:
        numero = int(input("inserte un numero : "))
        
        
        if numero > 10:
            raise NumerUpTen
        
        print ("Numreo correcto")
        
        return True
    except TypeError:
        print ("No ha introducido un numero")
        return False
    except ValueError:
        print ("No ha introducido un numero entero")
        return False
    except NumerUpTen:
        print ("El numero no puede ser mayor de 10")
        return False
        
numCorrecto = False  
while numCorrecto == False:
    numCorrecto = MyFuntion()
        
        
    