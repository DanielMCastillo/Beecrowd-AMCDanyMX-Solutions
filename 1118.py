def calculo():
    while True:
        total = []
        count = 0

        while count < 2:
            number = float(input())

            if number < 0 or number > 10:
                print("nota invalida")
            else:
                total.append(number)
                count += 1

        suma = sum(total)
        promedio = suma / len(total)
        print(f'media = {promedio:.2f}')

        print("novo calculo (1-sim 2-nao)")
        new = int(input())

        while new not in [1, 2]:
            print("novo calculo (1-sim 2-nao)")
            new = int(input())

        if new == 2:
            break

calculo()
