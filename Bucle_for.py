#antes
"""
for x in range(3):
    nested = []
    matrix.append(nested)
    for row in range(4):
        nested.append(0)
"""

#Verisión optimizada
#Ejemplo listas de listas con compresión de listas
matrix = [[0 for col in range(4)] for row in range(3)]

print(matrix)

