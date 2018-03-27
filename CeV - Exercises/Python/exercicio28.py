
from random import randint
from time import sleep

computador = randint(0,5) #Faz o computador rodar a roleta

print('-=-'*20)
print('Vou pensar em um número entre 0 e 5')
print('-=-'*20)

jogador = int(input('Em que número eu pensei? '))
print('Processando....')
sleep(3)
if jogador == computador:
    print('Parabens você me venceu')
else:
    print('Ganhei !!')


print('Pensei no número : {} ' .format(computador))
