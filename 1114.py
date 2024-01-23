passwd = 2002


while True:
    n = int(input())
    
    if n != passwd:
        print("Senha Invalida")

    elif(n == passwd):
        print("Acesso Permitido")
        break
    
        