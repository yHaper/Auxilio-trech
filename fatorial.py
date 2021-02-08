numero = int(input('\033[0;36mDigite um numero:\033[m '))
fatorial = numero
contador = 1
while (numero-contador)>1:
	fatorial = fatorial*(numero-contador)
	contador += 1
print('{0}! = {1}'.format(numero,fatorial))