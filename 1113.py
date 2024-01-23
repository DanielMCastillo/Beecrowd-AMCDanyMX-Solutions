while True:
    try:
        m, n = map(int, input().split())

        if m == n:
            break  # Salir del bucle si los valores son 2 y 2

        if m > n:
            print("Decrescente")
        else:
            print("Crescente")

    except EOFError:
        break  # Salir del bucle si se alcanza el final del archivo de entrada
