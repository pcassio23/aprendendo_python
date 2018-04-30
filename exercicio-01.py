## Sorteie 10 inteiros entre 1 e 100 para uma lista e descubra o maior e o menor valor sem
## usar a funcao max e min

import random

lista = []
maximo = 1
minimo = 100

for i in range (10):
    random.seed()
    lista.append(random.randrange(1,100))

for l in lista:
    if(l) > maximo:
        maximo = l

for n in lista:
    if(n) < minimo:
        minimo = n

for l in lista:
    print(l)

print('O maior valor é: ', maximo , ' o menor valor é: ', minimo)            