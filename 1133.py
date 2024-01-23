def main():
    x = int(input())
    y = int(input())
    
    # Asegurar que x sea menor que y
    if x > y:
        x, y = y, x
    
    # Iterar desde x hasta y (incluyendo y)
    for i in range(x+1, y):
        # Verificar si el resto de la división por 5 es igual a 2 o 3
        if i % 5 == 2 or i % 5 == 3:
            print(i)

if __name__ == "__main__":
    main()
