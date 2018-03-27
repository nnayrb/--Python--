distancia = float(input('Qual a distancia da viagem?: '))
print(' Você está prestes a começar a viagem de {} KM'.format(distancia))

if distancia <= 500:
    preço = distancia * 0.50
else:
    preço = distancia * 0.45
print(' E o preço da sua passagem será R$ {:.2f}'.format(preço))