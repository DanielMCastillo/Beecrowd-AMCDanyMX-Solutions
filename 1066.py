negativos = 0 
positivos = 0
par = 0
impar = 0


for i in range(5):
    x = int(input())
    
    if x %2 == 0:
        par +=1
    else:
        impar +=1 
    
    if x > 0:
        positivos+=1
    elif x<0:
        negativos+=1
    
    
print(par, "valor(es) par(es)")
print(impar, "valor(es) impar(es)")
print(positivos, "valor(es) positivo(s)")
print(negativos, "valor(es) negativo(s)")
