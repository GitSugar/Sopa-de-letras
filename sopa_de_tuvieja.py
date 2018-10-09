from random import *


#Inicializa el tablero. kpo
def init_tablero(longitud):
	f = longitud + randint(2,10)
	return ((["-"] * pow(f,2)), f)

def maximo(lista):
	n=i=0
	for i in range(0,len(lista)):
		if len(lista[i])>n:
			n = len(lista[i])
	return n

#if sepasa then true else false
def sepasa?(ori,pos,lon):
	if:
	elif:
	else:

def sopa_de_letras(lista):
	while lista!=[] :
		tablero = init_tablero(maximo(lista))
		ori = choice("Vertical","Horizontal","Diagonal")
		pos = randint(0, len(tablero[0])
		palabra = choice(lista)
		if(ori == "Horizontal"):
			while sepasa?(ori, pos, len(palabra)):
				pos = randint(0, len(tablero[0])
			check
			
		elif(ori == "Vertical"):
		else:
		lista = [elemento for elemento in lista if not (elemento == palabra)]
		


#opcion 1: te hace la sopa de letras
#opcion 2: te busca las palabras de la lista en la sopa de letras
def main():
	display="MENU\n1.-Ingrese lista palabras\n2Ingrese lista de palabras y sopa de letras\n0.Salir del programa\n*Ingrese una opciòn> "
	menu=int(input(display))
	while menu!=0:
		if menu==1 :
			lista=int(input("<ingrese una lista con las palabras para la sopa>"))
			sopa_de_letras(lista)
		else:
			lista=int(input("<ingrese una lista con las palabras para la sopa>"))
			sopa_de_letras_check(lista)
	print("Saliendo del programa")

#Terminar la salida grafica del tablero xddd
def prueba():
	tablero = init_tablero(16)
	for i in range(0, len(tablero[0])):
		if i%tablero[1] == 0:
			print(tablero[0][i],"\n")			
		else:
			print(tablero[0][i])

main()
