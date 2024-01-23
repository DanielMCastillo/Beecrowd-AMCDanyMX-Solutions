def main():
    n = int(input())
    
    total_cobaias = 0
    total_coelhos = 0
    total_ratos = 0
    total_sapos = 0
    
    for _ in range(n):
        entrada = input().split()
        amount, animal_type = int(entrada[0]), entrada[1]

        total_cobaias += amount

        if animal_type == 'C':
            total_coelhos += amount
        elif animal_type == 'R':
            total_ratos += amount
        elif animal_type == 'S':
            total_sapos += amount

    print("Total: {} cobaias".format(total_cobaias))
    print("Total de coelhos: {}".format(total_coelhos))
    print("Total de ratos: {}".format(total_ratos))
    print("Total de sapos: {}".format(total_sapos))

    percentual_coelhos = (total_coelhos / total_cobaias) * 100
    percentual_ratos = (total_ratos / total_cobaias) * 100
    percentual_sapos = (total_sapos / total_cobaias) * 100

    print("Percentual de coelhos: {:.2f} %".format(percentual_coelhos))
    print("Percentual de ratos: {:.2f} %".format(percentual_ratos))
    print("Percentual de sapos: {:.2f} %".format(percentual_sapos))

if __name__ == "__main__":
    main()
