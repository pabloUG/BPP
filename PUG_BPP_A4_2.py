L = (3, 4, 8, 5, 5, 22, 13)

def descomposicion (num: int) -> int:
    numAux = num
    cont   = 0
    if num == 1:
        return num
    else:
        while numAux > 0:
            if num%numAux == 0:
                cont += 1
            numAux -= 1
        
    if cont == 2:
        return num
    else:
        return 0  
          
LPrimos = filter(descomposicion ,L)

print(list(LPrimos))