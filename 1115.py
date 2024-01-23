while True:
    
    m, n = map(int, input().split())
    
    if(m == 0 or n == 0):
        break

    elif(m > 0 and n >0):
        print("primeiro")
    
    elif(m <0 and n> 0):
        print("segundo")
    
    elif(m <0 and n <0):
        print("terceiro")
    
    else:
        print("quarto")
    

        