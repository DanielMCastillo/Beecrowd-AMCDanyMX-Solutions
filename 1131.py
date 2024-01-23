
ganados_gremio = 0
ganados_inter = 0
partidos = 0
empates = 0

while True:
    m, n = map(int, input().split())
    
    if m > n:
        ganados_inter+=1
    elif n>m:
        ganados_gremio+=1
    elif m == n:
        empates+=1
    
    print("Novo grenal (1-sim 2-nao)")
    new = int(input())
    partidos+=1

    while new not in [1, 2]:
        print("Novo grenal (1-sim 2-nao)")
        new = int(input())

    if new == 2:
        break

print(f'{partidos} grenais')
print(f'Inter:{ganados_inter}')
print(f'Gremio:{ganados_gremio}')
print(f'Empates:{empates}')

if ganados_inter > ganados_gremio:
    print("Inter venceu mais")
else:
    print("Gremio venceu mais")
