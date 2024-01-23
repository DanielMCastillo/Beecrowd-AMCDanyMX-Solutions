n = int(input())

while(n>0):
    # Calcular el promedio ponderado
    numbers = list(map(float, input().split()))
    weighted_average = (numbers[0] * 2 + numbers[1] * 3 + numbers[2] * 5) / 10
    print(f'{weighted_average:.1f}')
    n-=1


