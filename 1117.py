total = []

while True:
    number = float(input())
    
    if number < 0 or number > 10:
        print("nota invalida")
    else:
        total.append(number)
    
    if len(total) == 2:
        break

suma = sum(total)
promedio = suma / len(total)

print(f'media = {promedio:.2f}')
