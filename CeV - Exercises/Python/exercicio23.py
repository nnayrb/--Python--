a = int(input('primeiro valor :'))
b = int(input(' segundo valor : '))
c = int(input(' terceiro valor: '))
#verificando menor
if a<b and a<c:
    menor = a
if b<c and b<a:
    menor = b
if c<a and c<b:
    menor = c

if a>b and a>c:
    maior = a
if b>c and b>a:
    maior = b
if c>a and c>b:
    maior = c

print('O menor valor digitado foi {} e o maior foi {}'.format(menor, maior))
