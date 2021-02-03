import os

os.system("clear")

print("\033[1;34mBem vindo a calculadora de burros \033[m\n")

calc = input("Qual operação deseja fazer? \n\n\033[0;36m+ = Adição \n- = Subtração \n* = Multiplicação \n/ = Divisão \n** = Potencia\033[m\ns = Sair\n\n==> ")

if calc == 's' or calc == 'S':
	print("Até logo burrão")
	 
elif calc == '+' or calc == '-' or calc == '*' or calc == '/' or calc == '**':
	num1 = int(input("==> "))
	num2 = int(input("==> "))
else:
	print("invalido")

if calc == '+':
   total = num1 + num2
   print(total)
elif calc == '-':
	total = num1 - num2
	print(total)
elif calc == '*':
	total = num1 * num2
	print(total)
elif calc == '/':
	total = num1 / num2
	print(total)
elif calc == '**':
	total = num1 ** num2
	print(total)