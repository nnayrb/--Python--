leia = input('Digite qualquer coisa : ')
print('O tipo primitivo desse programa é : ' ,  type(leia))
print(' Possui espaços? : ', (leia.isspace()))
print(' Está em Caps?: ', (leia.isupper()))
print(' É número?: ', (leia.isnumeric()))
print(' É alfanumérico?: ', (leia.isalnum()))
print(' É alfabético?: ', (leia.isalpha()))
print(' Está em letras minusculas?: ', (leia.islower()))
print('Está capitalizada?: ', (leia.istitle()))


