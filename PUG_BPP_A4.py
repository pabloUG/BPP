import pdb
pdb.set_trace()

mayor_L1 = 0
mayor_L2 = 0
mayor_L3 = 0
count = 0
LL = [(2,4,1),(1,2,3,4,5,6,7,8),(100,250,43)]

for l1 in LL: 
    for l2 in l1:
        if count == 0:
            if mayor_L1 < l2:
                mayor_L1 = l2
        
        if count == 1:
            if mayor_L2 < l2:
                mayor_L2 = l2
                
        if count == 2:
            if mayor_L3 < l2:
                mayor_L3 = l2
    
    count += 1
    
print(f'El mayor de la lista 1 es {mayor_L1}')
print(f'El mayor de la lista 2 es {mayor_L2}')
print(f'El mayor de la lista 3 es {mayor_L3}')
        
if __name__ == '__main__':
    pass