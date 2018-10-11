'''
Manejo de Archivos en Py3

Archivos de texto .txt

Abrir
------
string string -> file
open(<ruta delarchivo>, <r/r+/w/w+/a/a+>) <read, write, append>

archivo = open("hola.text", "r") <abre el hola.txt en lectura>

Para crear un archivo basta con abrirlo en modo escritura cuando el archivo no existe

Leer
-----

[metodo 1: Read]
number -> string
archivo.read(n) <lee n bytes del archivo en cuestion>
archivo.read(5) <lee 5 caracteres del archivo y se queda en esa posicion>

[metodo 2: readline]
void -> string
archivo.readline <lee hasta un salto de linea (incluido)>

[metodo 3: readlines]
void -> string
archivo.readlines <devuelve todas las lineas del archivo>

[metodo 4: recomendado por la comunidad (file in for)]

for line in archivo <archivo se puede convertir a lista haciendo list(archivo)>
    print line      <imprime las lineas del archivo separado por 1 espacio>


Escribir
--------
open("hola2.txt", "w")

string -> Number
archivo.write(<string a añadir>)


Cerrar
------
archivo.close() <cierra el archivo para terminarde escribirlo>

archivo.closed <True si esta cerrado y False sino>

----
Para resetear el puntero de lectura basta con cerrar y abrir el archivo 
xdddddd
'''
from random import *
from math import *


'''
Inicia el tablero, dependiendo de la longitud de la palabra mas larga, da un margen de 6 o 7 de ancho
Devuelve el tablero y la longitud de la fila.
'''
def init_tablero(longitud):
	if (longitud%2==0): longitud += 6
	else: longitud += 7
	return ((["-"] * longitud ** 2), longitud)

'''
Retorna el numero de caracteres de la palabra con mas caracteres de la lista
'''
def maximo(lista):
	n=i=0
	for i in range(0,len(lista)):
		if len(lista[i])>n:
			n = len(lista[i])
	return n

def calc_margen_actual(margen, posicion):
    return ((position // margen)+1)*margen
    
    

'''
Si la palabra es horizontal solo basta con sumarle a n la longitud del string
si casa empezase en el casillero 7 de un tablero 5x5 tendriamos que 
c = n + 0 = 7
a = n + 1 = 8
s = n + 2 = 9
a = n + 3 = 10

posFin = n + len(palabra) - 1 <ya que se cuenta la primera posicion como n>

La formula para calcular el vertical creo que es posFin= len(plabra)*margen + (posIni - margen)
Entonces si, por ejemplo, casa empezase en la posición 8 de un tablero 5x5
tendria las siguientes posiciones
c = 1*5 + 3 = 8
a = 2*5 + 3 = 13
s = 3*5 + 3 = 18
a = 4*5 + 3 = 23
que se corresponden con la realidad para una palabra vertical
Como se ve son todos multiplos de la longitud del tablero mas un offset, en este caso 3
ya que el tablero era de 5x5.
'''
def sepasa(ori,posIni,lon,margen_tablero):
	margen = calc_margen_actual(margen_tablero)
	if(ori == "Horizontal"):
		if(posIni + lon - 1 > margen):
			return True
	elif(ori == "Vertical"):
		posF_vert = lon*margen_tablero +(posIni - margen)
		if(posF_vert > margen or posF_vert > margen_tablero ** 2):
			return True
	elif(ori == "Diagonal Inf"):
        posF_DiagInf = (posIni + (lon-1)*(margen_tablero+1)
        if(posF_DiagInf > margen or posF_DiagInf > margen_tablero ** 2):
            return True
	else:
        posF_DiagSup = posIni - (margen_tablero -1) * lon 
	return False

def sopa_de_letras(lista):
	while lista!=[] :
		tablero = init_tablero(maximo(lista))
		ori = choice("Vertical","Horizontal","Diagonal Sup","Diagonal Inf")
		pos = randint(0, len(tablero[0]))
		palabra = choice(lista)
		sen = choice("+","-")

		if(sen=="-"):
			palabra = inv(palabra)

		if(ori == "Horizontal"):
			while sepasa(ori, pos, len(palabra)):
				pos = randint(0, len(tablero[0]))
			poner_palabra(ori, pos, palabra, tablero)

		elif(ori == "Vertical"):
			while sepasa(ori, pos, len(palabra)):
				pos = randint(0, len(tablero[0]))
			poner_palabra(ori, pos, palabra, tablero)

		elif(ori == "Diagonal Inf"):
			while sepasa(ori, pos, len(palabra)):
				pos = randint(0, len(tablero[0]))
			poner_palabra(ori, pos, palabra, tablero)

		else:
			while sepasa(ori, pos, len(palabra)):
				pos = randint(0, len(tablero[0]))
			poner_palabra(ori, pos, palabra, tablero)

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
