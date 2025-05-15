#Listas anidadas
list_of_lists = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flatten_lista = [x for y in list_of_lists for x in y]
print(flatten_lista)

#otro ejemplo
matrix = [[1,2,3],[4,5,6],[7,8,9]]

nueva_matrix = [[row[i] for row in matrix] for i in range(3)]
print(nueva_matrix)


#Ejemplo de listas anidadas código completo
transposed = [[1,2,3],[4,5,6],[7,8,9]]

for i in range(3):
     transposed_row = []
     for row in matrix:
            transposed_row.append(row[i])
     transposed.append(transposed_row)
print(transposed)

#c+odigo optimizado 
transposed_row=[[row[i] for row in transposed]for i in range(3)]
print(transposed_row)

