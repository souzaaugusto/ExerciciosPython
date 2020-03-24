#JOGO JO KEN PO feito no curso de Python do professor Gustavo Guanabara

#---------Importação de bibliotecas:
from random import randint
from time import sleep

#---------Variáveis:
itens = ('Pedra', 'Papel', 'Tesoura')
computador = randint(0, 2)

#---------Escolha da jogada:
print('''Suas opções:
[0] PEDRA
[1] PAPEL
[2] TESOURA''')
jogador = int(input('Qual sua jogada?: '))

#---------Inicio do jogo:
print('JO')
sleep(1)
print('KEN')
sleep(1)
print('PO')
print('-=' * 11)
#----------As escolhas dos jogadores:
print('Computador jogou {}'.format(itens[computador]))
print('Jogador jogou {}'.format(itens[jogador]))
print('-=' * 11)

#----------Resultado:
if computador == 0:
    if jogador == 0:
        print('EMPATE')
    elif jogador == 1:
        print('Você venceu!')
    elif jogador == 2:
        print('Computador venceu!')
    else:
        print('Jogo inválido')
elif computador == 1:
    if jogador == 1:
        print('EMPATE')
    elif jogador == 0:
        print('Computador venceu')
    elif jogador == 2:
        print('Você venceu!')
    else:
        print('Jogo inválido')
elif computador == 2:
    if jogador == 2:
        print('Empate')
    elif jogador == 0:
        print('Você venceu!')
    elif jogador == 1:
        print(('Computador venceu!'))

