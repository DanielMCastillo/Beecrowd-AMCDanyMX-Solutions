n  = int(input())

while(n>0):
    numbers = int(input())
    
    if numbers %2 == 0 and numbers >0:
        print("EVEN POSITIVE")
    elif(numbers %2 != 0 and numbers >0):
        print("ODD POSITIVE")
    elif(numbers %2 != 0 and numbers <0):
        print("ODD NEGATIVE")
    elif(numbers %2 == 0 and numbers <0):
        print("EVEN NEGATIVE")
    else:
        print("NULL") 
    n -=1
    

    