print("Ejercicio 1")
print("VERSIÓN CON UNA FUNCIÓN LAMBDA")
# Initialize the `kilometer` list 
kilometer = [39.2, 36.5, 37.3, 37.8]

# Construct `feet` with `map()`
feet = map(lambda x: float(3280.8399)*x, kilometer)

# Print `feet` as a list 
print(list(feet))

print("VERSIÓN CON UNA COMPRENSION DE LISTA ")

feet2 = [float(3280.8399)*x for x in kilometer]
print(feet2)