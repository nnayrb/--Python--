largura = float(input('Largura da parede : '))
altura = float(input(' Altura da Parede : '))

are = largura*altura
lit = are/2
print('Sua parede tem a dimensão de {}x{} e sua área é de {}m².'.format(largura, altura, are))
print('para pintar essa parede, você precisara de {}L de tinta'.format(lit))