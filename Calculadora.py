def novamente():
    calc_novamente = input('''
Deseja calcular novamente?
Digite S para sim e N para não.
''')

    if calc_novamente.upper() == 'S':
        calculo()
    elif calc_novamente.upper() == 'N':
        print('Até mais.')
    else:
        novamente()


def calculo():
    operacao = input('''
Escolha uma operação matemática:
+ para adição
- para subtração
* para multiplicação
/ para divisão
''')

    number_1 = int(input('Informe um primeiro número: '))
    number_2 = int(input('Informe um segundo número: '))

    if operacao == '+':
        print('{} + {} = '.format(number_1, number_2))
        print(number_1 + number_2)

    elif operacao == '-':
        print('{} - {} = '.format(number_1, number_2))
        print(number_1 - number_2)

    elif operacao == '*':
        print('{} * {} = '.format(number_1, number_2))
        print(number_1 * number_2)

    elif operacao == '/':
        print('{} / {} = '.format(number_1, number_2))
        print(number_1 / number_2)

    else:
        print('Você escolheu uma operação inválida, tente novamente.')

    novamente()

calculo()