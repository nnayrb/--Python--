print('-=-'*20)
print('Analisador de Triangulo')
print('-=-'*20)
r1 = float(input("Primeiro segmento : "))
r2 = float(input("Segundo Segmento : "))
r3 = float(input("Terceiro Segmento: "))

if r1< r2 + 3 and r2 < 1 + r3 and r3 < r1 + r2:
    print('os segmentos acima podem formar triangulo')
else:
    print('os segmentos acima não podem formar triangulo')