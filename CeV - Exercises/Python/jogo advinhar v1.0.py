from random import randint
from time import sleep
from termcolor import colored
computador = randint(0, 3)
print('\033[34;40m-=-\033[m' * 20)
print('Vou pensar em um número entre 0 e 8. Tente advinhar...')
print('\033[34;40m-=-\033[m' * 20)
jogador = int(input('Em que número eu pensei??')) #Jogador tentar advinhar
print('PROCESSANDO...')
sleep(3)
print(' Pensei no número {}'.format(computador))#faz o computador "pensar"
if jogador == computador: #orientação
    print('Parabens !! você conseguiu advinhar e me venceu !!')
else:
    print('Ganhei ! de você bobão, viu como sou um AI inteligente? :P ')