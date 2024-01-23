n = int(input())

while(n>0):
    x, y = map(int, input().split())

    if(y==0):
        print("divisao impossivel")
    elif(x == 0):
        print(0.0)
    else:
        resultado = x/y
        print(resultado)


    n-=1
    
    

        