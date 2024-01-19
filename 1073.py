n = int(input())

lista = []
for i in range(1, n+1):
    if i % 2== 0:
        lista.append(i)

for j in lista:
    print(f"{j}^2 = {j ** 2}")