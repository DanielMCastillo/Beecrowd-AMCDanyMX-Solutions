rn = int(input())
cuenta = 0
nocuenta = 0

while(rn>0):
    n = int(input())
    
    if n >= 10 and n <= 20:
        cuenta+=1
    else:
        nocuenta +=1
        
    rn -= 1

print(str(cuenta) + " in")
print(str(nocuenta) + " out")
