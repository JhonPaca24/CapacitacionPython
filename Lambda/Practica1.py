"""
Cuándo usar las funciones Lambda
Lógica corta y simple. Ideal para operaciones concisas que no requieren una definición de función completa.

Funciones de orden superior. Trabajar eficazmente como argumentos para funciones de orden superior como map(), filter(), o sorted().

Funciones temporales (throwaway). Útil cuando se necesita una función solo una vez, y definiéndola con def desordenaría innecesariamente el código.

Mejora de la legibilidad. Adecuado para tareas simples donde el uso de una función lambda mantiene el código compacto y fácil de seguir.

Cuándo evitar las funciones Lambda
Lógica compleja o multilínea. Los Lambdas se limitan a una sola expresión y pueden volverse ilegibles rápidamente para operaciones más complejas.

Funciones reutilizables o nombradas. Si la función necesita ser reutilizada o se beneficia de un nombre descriptivo, un estándar def la función es más apropiada.

Depuración o documentación. Las funciones Lambda carecen de la capacidad de incluir docstrings y pueden ser más difíciles de depurar en comparación con las funciones nombradas."""

#Dado un número, encuentra su cuadrado.
num = int(input("Ingrese un número: "))
cuadrado = lambda x: x**2
print(f"El cuadrado de {num} es: {cuadrado(num)}")

#Dados dos números, encuentra el más grande.
num2 = int(input("Ingrese otro número: "))
mayor = lambda x,y: x if x>y else y 
print(f"El número mayor entre {num} y {num2} es: {mayor(num,num2)}")

#Dado un número, compruebe si es impar.
impar = lambda x: False if x%2==0 else True
print(f"El número {num} es impar: {impar(num)}")

#Dada una lista de enteros positivos, filtre todos los números impares.
lista_enteros_positivos = [1, 2, 3, 4, 5]
nueva_lista = list(filter(lambda x: x%2!=0, lista_enteros_positivos))
print(f"Lista de números impares: {nueva_lista}")

#Ordene una lista de tuplas de 3 elementos usando sus terceros elementos.
lista_tuplas = [(1,2,5), (2,3,4), (5,6,7)]
nuevas_tuplas = sorted(lista_tuplas, key =lambda x: x[2])
print(f"Lista de tuplas ordenadas por el segundo elemento: {nuevas_tuplas}")

correo = "user@example.com"
direccion = lambda x: x.split('@')[1]
print(f"El nombre de usuario es: {direccion(correo)}")