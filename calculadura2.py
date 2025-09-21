while True:
    numero_1 = input('Digite um número: ')
    numero_2 = input('Digite outro número: ')
    operador = input('Digite o operador (+-/*): ')

    numeros_validos = None
    numero_1_float = 0
    numero_2_float = 0

    try:
        numero_1_float = float(numero_1)
        numero_2_float = float(numero_2)
        numeros_validos = True

    except:
        numeros_validos = None
    if numeros_validos is None:
        print('[ERRO] Número(s) invalidos!')
        continue

    operadores_permitidos = '+-/*'

    if operador not in operadores_permitidos:
        print('[ERRO] Operador invalido!')
        continue

    if len(operador) > 1:
        print('Digite apenas um operador.')
        continue

    print('Resultado:')
    if operador == '+':
        print(numero_1_float + numero_2_float)
    elif operador== '-':
        print(numero_1_float - numero_2_float)
    elif operador == '/':
        if numero_1_float == 0:
            print('[ERRO] Não é possivel dividir por zero!')
        else:
            print(numero_1_float / numero_2_float)
    elif operador == '*':
        print(numero_1_float * numero_2_float)
    else:
        print('Não sei o que você fez pra chegar aqui.')
    
    sair = input('Quer sair? [s]im: ').lower().startswith('s') 
    if sair is True:
     break