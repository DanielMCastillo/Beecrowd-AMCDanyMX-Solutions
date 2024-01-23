alcohol = 0
gasolina = 0
diesel = 0

while True:
    type_customer = int(input())
    
    if type_customer <1 or type_customer >4:
        pass
    if type_customer == 1:
        alcohol+=1
    elif type_customer == 2:
        gasolina+=1
    elif type_customer ==3:
        diesel+=1
    elif type_customer == 4:
        break

print("MUITO OBRIGADO")
print(f'Alcool: {alcohol}')
print(f'Gasolina: {gasolina}')
print(f'Diesel: {diesel}')


