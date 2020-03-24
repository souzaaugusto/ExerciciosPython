#Simples código de conversão de base numérica feita no curso de Python do Professor Gustavo Guanabara

#--------Escolha de um numero qualquer:
num = int(input('Digite um número: '))

#--------Escolha da base numerica:
print(''' Escolha uma das bases para conversão:
[1] para binário
[2] para octal
[3] para hexadecimal''')

#------- Resutado da conversão escolhida:
opção = int(input('Sua opção: '))
if opção == 1:
    print('{} convertido para binário é igual a {}'.format (num, bin(num)))
elif opção == 2:
    print('{} convertido para octal é igual a {}'.format (num, oct(num)))
elif opção == 3:
    print('{} convertido para hexadecimal é  igual a {}'.format (num, hex(num)))
