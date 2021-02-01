import os

print(""" \033[0;32m
=====> yHaper AUX <=====
[01] apt upgrade -y && apt update -y
[02] ping
[03] git clone
[04] instalar python
[05] instalar ipython
[06] sair
=====> yHaper AUX <=====
\033[m """)

aux = input("\033[1;32m~ \033[m")

if aux == '01' or aux == '1':
	print(" Atualizando ")
	os.system("clear")
	os.system("apt update -y && apt upgrade -y")
	os.system("clear")
	
elif aux == '02' or aux == '2':
	os.system("clear")
	p = "ping "
	a = input("==> ")
	b = p+a
	os.system(b)
	
elif aux == '03' or aux == '3':
    os.system("clear")
    git = "git clone "
    clone = input("==> ")
    x = git+clone
    os.system(x)
    
elif aux == '04' or aux == '4':
	os.system("clear")
	os.system("apt install python -y && apt install pyhon2 -y")
	os.system("clear")
	
elif aux == '05' or aux == '5':
	os.system("clear")
	os.system("pip install ipython")
	os.system("clear")
	
elif aux == '06' or aux == '6':
	print("Volte sempre")