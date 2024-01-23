while True:
    m, n = map(int, input().split())

    if m <= 0 or n <= 0:
        break  # Salir del bucle si alguno de los valores es menor o igual a cero

    smallest = min(m, n)
    largest = max(m, n)

    sequence = list(range(smallest, largest + 1))
    sequence_str = ' '.join(map(str, sequence))

    sum_values = sum(sequence)

    print(f'{sequence_str} Sum={sum_values}')
