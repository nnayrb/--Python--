aluguel = int(input('Quantos dias alugados? : '))
kmro = int(input('KMs Rodados? : '))
pordia = aluguel*60 + (kmro * 0.15)
total = pordia
print('O total a pagar é : R${:.2f}'.format(total))
