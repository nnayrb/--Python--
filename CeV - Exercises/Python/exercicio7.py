n1 = int(input('Um Valor : '))
n2 = int(input('outro valor: '))
s = n1 + n2
m = n1 * n2
d = n1 / n2
di = n1 // n2
e = n1 ** n2
print('A soma vale {}, \n o produto é {} e \n a divisão é {:.3f}'.format(s, m, d), end='')
print(' Divisão inteira {} e potência {}'.format(di, e))