n = 100

numbers = []

while(n != 0):
    number = int(input())
    numbers.append(number)
    n-=1

maximo = max(numbers)
posicion_maximo = numbers.index(maximo)

print(maximo)
print(posicion_maximo+1)