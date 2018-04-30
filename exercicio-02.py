## Sorteie 20 inteiros entre 1 e 100 numa lista. Armazene os números pares na 
## lista PAR e os números ímpares na lista IMPAR. Imprima as Três listas

import random

pares = []
impares = []
lista = []

for i in range(20):
    lista.append(random.randint(1,100))

for l in lista:
    if(l % 2 == 0):
        pares.append(l)
    else:
        impares.append(l)

print('Lista geral')
for l in lista:
    print(l)

print()
print('Lista pares')    
for p in pares:
    print(p)

print()
print('Lista impares')
for i in impares:
    print(i)