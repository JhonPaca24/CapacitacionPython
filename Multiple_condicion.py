#Multiples condificones 
divided = [x for x in range(100) if x % 2 == 0 if x % 6 == 0]

print(divided)

# Con condiciones elif
nes_divide = [x+1 if x >= 120000 else x+5 for x in range(50)]
print(nes_divide)