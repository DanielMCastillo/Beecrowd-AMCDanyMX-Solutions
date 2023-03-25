x = int(input())
y = int(input())

# awsegurarnos del rango iniciando en x
if x > y:
    x, y = y, x

#Inicializar suma
suma = 0

# Iterar en el rango
#hacer la suma
for i in range(x, y+1, 2):
        suma += i


print(suma)
