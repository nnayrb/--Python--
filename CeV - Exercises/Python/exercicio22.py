nome = str(input('QUal é seu nome?'))
if nome == 'Bryann':
   print('Nome lindo'.format(nome))

elif nome == 'Pedro' or nome == 'Maria' or nome == 'Paulo':
    print('Seu nome é comum no Brasil.'.format(nome))

else:
    print('Seu nome é bem normal')

print('Tenha um bom dia. {}!'.format(nome))