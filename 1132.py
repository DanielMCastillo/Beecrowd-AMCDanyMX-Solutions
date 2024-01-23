def main():
    
    
    m = int(input())
    n = int(input())
    
    smallest = min(m, n)
    largest = max(m, n)
    
    lista = []
    
    for i in range(smallest, largest+1):
        if i % 13 != 0:
            lista.append(i)
    
    print(sum(lista))

if __name__ == "__main__":
    main()
