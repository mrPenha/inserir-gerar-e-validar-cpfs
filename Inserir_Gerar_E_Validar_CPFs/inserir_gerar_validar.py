import os
import random
os.system('clear')

lista_de_cpfs = []
cpf = []

while True:
    print('Opções: \n\n1 - Inserir CPF \n2 - Gerar CPFs aleatórios \n3 - Validar CPF \n4 - Imprimir lista de CPFs \n5 - Sair \n--------------------------')
    op = int(input('> '))

    if op == 1:
        os.system('clear')

        verdadeiro = True
        while verdadeiro:
            n = input('Digite seu CPF: ')

            for i in range(len(n)):
                cpf.append(n[i])

            cpf.insert(3, '.'), cpf.insert(7, '.'), cpf.insert(11, '-')
            new_cpf = ''.join(cpf)

            if new_cpf in lista_de_cpfs:
                print('\nCPF já cadastrado\n')
                input('Aperte ENTER para continuar...')

            else:
                lista_de_cpfs.append(new_cpf)
                verdadeiro = False

            cpf.clear()
            os.system('clear')

    elif op == 2:
        os.system('clear')

        qtd = int(input('Quantos CPFs gostaria de gerar? \n> '))
        for i in range(qtd):
            cpf = []
            for i in range(11):
                n = random.randint(0, 9)
                n = str(n)
                cpf.append(n)

            cpf.insert(3, '.'), cpf.insert(7, '.'), cpf.insert(11, '-')
            novo_cpf = ''.join(cpf)
            lista_de_cpfs.append(novo_cpf)
            cpf.clear()

        print('\nCPFs gerados com sucesso!\n')
        input('Aperte ENTER para sair...')
        os.system('clear')

    elif op == 3:
        os.system('clear')
        n = input('Digite seu CPF: ')
        os.system('clear')

        for i in range(len(n)):
            cpf.append(n[i])

        if len(cpf) == 11:
            cpf.insert(3, '.'), cpf.insert(7, '.'), cpf.insert(11, '-')
            new_cpf = ''.join(cpf)
            print(new_cpf)
            print('\nCPF VÁLIDO\n')

        else:
            cpf.insert(3, '.'), cpf.insert(7, '.'), cpf.insert(11, '-')
            new_cpf = ''.join(cpf)
            print(new_cpf)
            print('\nCPF INVÁLIDO\n')

        input('Aperte ENTER para sair...')
        os.system('clear')

    elif op == 4:
        os.system('clear')
        print('QTDE |   CPF')
        print('-----------------------')

        for i in range(len(lista_de_cpfs)):
            if i < 9:
                print(f'{i+1: }   |   {lista_de_cpfs[i]} ')
                print('\n-----------------------\n')
            else:
                print(f'{i+1:}   |   {lista_de_cpfs[i]} ')
                print('\n-----------------------\n')

        input('\nAperte ENTER para sair...')
        os.system('clear')

    elif op == 5:
        os.system('clear')
        print('FIM \n')
        break

    else:
        os.system('clear')
        print('Opção Inválida \n')
