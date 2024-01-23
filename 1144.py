def main():
    n = int(input())
    count = 0
    start = 1
    
    while count < n:
        end = start 
        mid = start * end
        print(f"{start} {mid} {end * mid}")
        print(f"{start} {mid+1} {mid * end+1}")
        
        
        start+=1
        count += 1

if __name__ == "__main__":
    main()
