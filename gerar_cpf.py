import random
import os
os.system('clear')

cpf = []
for i in range(14):
    if i == 3 or i == 7:
        cpf.append('.')

    elif i == 11:
        cpf.append('-')

    else:
        n = random.randint(0, 9)
        n = str(n)
        cpf.append(n)

novo_cpf = ''.join(cpf)

print('CPF:', novo_cpf)
print()
