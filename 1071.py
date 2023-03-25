x = int(input())
y = int(input())

# verificar que x es menor pera rango 1
if x > y:
    x, y = y, x

suma_de_impares = 0
for numeros in range(x+1, y):
    if numeros % 2 == 1:
        suma_de_impares += numeros

print(suma_de_impares)
