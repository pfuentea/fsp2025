
'''
for numero in range(5): #desde el 0 hasta <5
    print(f"numero={numero}")

for i in range(10):
    if i == 5:
        break
    print(i)
'''

# imprimiendo números impares
for i in range(10):
    if i % 2 == 0 : # si es par...continua       
        continue
    
    print(i) 

# imprimiendo números pares
for i in range(10):
    if i % 2 != 0 : # si es ipar...continua       
        continue
    
    print(i) 