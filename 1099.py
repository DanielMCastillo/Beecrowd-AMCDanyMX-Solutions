n = int(input())

while n > 0:
    numbers = list(map(int, input().split()))
    lista_impares = []

    x, y = min(numbers), max(numbers)

    for i in range(x+1, y):
        if i % 2 != 0:
            lista_impares.append(i)
    
    # Imprimir la suma total de números impares después de completar el bucle
    print(sum(lista_impares))
    
    n -= 1

    
    
    