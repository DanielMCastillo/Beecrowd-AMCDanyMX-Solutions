# Leer valor de x
x = int(input())

# Comprobar si x es par y hacerlo impar
if x % 2 == 0:
    x += 1

# imprimir los seis numeros consecutivos
# , incluyendo X si este es impar
for i in range(6):
    print(x)
    x += 2
