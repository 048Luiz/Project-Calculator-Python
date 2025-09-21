from math import sqrt

def calculator():
    print("Calculadora em Python")
    print("(Operações disponíveis: \n '+' Adição \n '-' Subtração \n '*' Multiplicação \n '/' Divisão) \n 'E' para cancelar.")

# '+' Adição
# '-' Subtração
# '*' Multiplicação
# '/' Divisão
# 'E' Sair da operação

while True:
    number_1 = float(input('Digite o primeiro número: '))
    operator = input('Digite o operador (+, -, *, /): E para cancelar. ')

    if operator.upper() == 'E':
        print("Operação encerrada!")
        break

    number_2 = float(input('Digite o segundo número: '))

    if operator == '+':
        result = number_1 + number_2
    elif operator == '-':
        result = number_1 - number_2
    elif operator == '*':
        result = number_1 * number_2
    elif operator == '/':
        if number_2 == 0:
            print('[ERRO] Divisão por zero não é permitida!')
            continue
        else:
            result = number_1 / number_2
    else:
        print('[ERRO] Operador inválido!')
        continue

    print(f'Resultado: {result:.2f}')

calculator()