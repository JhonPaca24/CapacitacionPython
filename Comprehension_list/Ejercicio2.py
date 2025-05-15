#usando filtrado

numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares1 = list(filter(lambda x: x % 2 == 0, numeros))
print(numeros_pares1)

#usando map 
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
numeros_pares2 = list(map(lambda x: x * 2, numeros))
print(numeros_pares2)

# usando reduce 

from functools import reduce
numeros = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]   
suma = reduce(lambda x, y: x + y, numeros)
print(suma)