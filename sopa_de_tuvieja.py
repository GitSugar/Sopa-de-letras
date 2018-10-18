
"""
<<<<SOPA DE LETRAS>>>>

Nota= para representar la sopa de letras se acordó utilizar una única lista y para la interfaz gráfica se presenta esa misma lista dividía teniendo en cuanta la longitud obtenida en la función init_tablero.
Nota2= a las funciones donde intervien la funcion random y sus variantes no se les ha hecho casos de pytest

<===Funciones adicionales===>

1º colocar_letras_faltantes (coloca las letras faltantes de la sopa de letras una vez introducidas las palabras)
2º init_tablero (genera el tablero deacuerdo a un cierto numero y arma una tupla con el tablero y su ancho)
3º salida (no permite representar la sopa de letras de forma grafica)
4º maximo (nos brinda la longirud de la palabra mas larga de una lista de palabras para armar la sopa)
5º plain (nos permite convertir una lista de lista en una unica lista con los elementos de cada una de las listas interiores)
6º get_lista(nos permite pasar las palabras escritas en el archivo lista_de_palabras.txt en una lista )
7º import_export_sopa ( leer el archivo que contiene a la sopa de letras y transformarla en una lista, devolviendo una tupla con la lista en cuestion y su ancho )
8º calc_margen_actual (calcula el limite o margen del tablero)
9º sepasa(actua como predicado para ver si la palabra a colocar se sale de los margenes del tablero)
10º poner_palabra(coloca las palabras dentro de el tablero de al sopa de letras)
11º invertir_palabra (invierte una palabra cualquiera)
12º sopa_de_letras(compone una sopa de letras a paratir de una lista de palabras)
13º diferencia_simentrica_listas(actua como la diferencia simetrica de conjutos pero sobre listas)
14º cordenadas_palabras (nos permite obtener la fila y la columna de la primera letra de una palabra)
15º palabras_encontradas (devuelve las palabra encontradas dentro de la sopa)
16º eleccion (nos da el sentido de una palabra)
17º generar_cords(nos da los datos de las palabras encontradas)
18º sopa_de_letras_check (busca palabras dentro de una sopa de letras)


<=====Función Principal=====>

1º main(función principal que nos permite inicializar el programa)

"""
#<===Funciones adicionales===>

from random import *
archivo=open("sdl.txt","a+")
archivo.close()
archivo=open("lista_de_palabras.txt","a+")
archivo.close()

'''colocar_letras_faltantes: list ->list'''
def colocar_letras_faltantes(tablero):
	"""
	La funcion  colocar_letras_faltantes recibe una lista(tablero) que es el tablero a completar que ya dispone de carcteres en su interior (donde ya han sido colocadas las palabras dispuestas por
	el usuario) y se encarga de completar los espacios vacios de la lista (todas aquellas posiciones que contengan este "-" carcater) con cualquier letra dentro del abecedario.
	"""
	for i in range(0,len(tablero)):
		if tablero[i]=="-":
			letra=choice(["a","b","c","d","e","f","g","h","i","j","k","l","m","n","ñ","o","p","q","r","s","t","u","v","w","x","y","z"])
			tablero[i]=letra
	return tablero


'''init_tablero: number -> list'''
def init_tablero(longitud):
	"""
   La funcion init_tablero recibe una longitud (un numero natural) y devuelve una tupla de dos elementos , el primero es una lista de (longitud + 6) al cuadrado de
   elementos = "-" en el caso de que sea par o (longitud + 7) al cuadrado de elementos= "-"  en el caso de que sea
   impar (esta función nos brinda la capacidad de crear un tablero lo suficientemente grande para la sopa de letras), y el segundo es el ancho que tendra el tablero de la sopa
   """
	if longitud==0:
		return ([],0)
	if (longitud%2==0):
		longitud += 6
	else: longitud += 7

	return (["-"] * longitud ** 2, int(longitud))

def test_init_tablero():
   assert init_tablero(8) == (["-"] * 196,14)
   assert init_tablero(9) == (["-"] * 256,16)
   assert init_tablero(0) == ([],0)



'''salida : list->int  -> list'''
def salida(lista, margen):
	"""
	La función salida actúa como nuestra interfaz gráfica de la sopa de letras a partir del tablero
	compuesto por la función init_tablero (cabe aclarar que es solo un interfaz del sistema
	su única función es lograr que el usuario pueda ver el tablero de la sopa de letras , es solo estético)
	"""
	out=[]
	for i in range(0,len(lista)-1,margen):
		out.append(lista[i:i+margen])		
	print(*out, sep='\n')
	

''' maximo: lista -> number '''
def maximo(lista):
	"""
	La función maximo recibe una lista de cadenas, toma la cadena más larga de la lista y devuelve
	su longitud o tamaño como un número real (esta función es utilizada en la función sopa_de_letras
	para obtener el tamaño de nuestro tablero)
	"""
	cont=0
	for i in range(0,len(lista)):
		if len(lista[i])>cont:
			cont = len(lista[i])
	return cont

def test_maximo():
	assert maximo(["pueblo","12","casa"])== 6
	assert maximo(["pueblo", "1234567", "casa"]) == 7
	assert maximo([]) == 0




'''plain: lista -> lista'''
def plain(lista):
	"""
	La funcion plain recibe una lista (lista de listas) y devuelve una unica lista con los elementos de cada una de las listas interiores
	(Esta funcion es utilizada respecto al archivo lista_de_palabras)
	"""
	lista_nueva = []
	for i in range(0, len(lista)):
		for pos in range(0, len(lista[i])):
			lista_nueva.append(lista[i][pos])
	return lista_nueva

def test_plain():
	assert plain([["gato"], ["sopa"], ["palabra"]]) == ["gato","sopa","palabra"]
	assert plain([["a"], ["b"]]) == ["a","b"]
	assert plain([["543534"], ["numero"], ["¡!"]]) == ["543534","numero","¡!"]




#r=read Xd
def get_lista(archivo):
	"""
	La funcion accede al archivo lista_de_palabras.txt y toma las palabras de cada nivel y las agrupa en una lista
	La cantidad de elementos de la lista depende de la cantidad de enters que tenga el archivo
	"""
	lista= []
	for linea in list(archivo):
		linea = linea.strip()
		lista.append(linea)
	archivo.close()
	return lista



def import_export_sopa(tablero, n):
	"""
	los valores por default de esta funcion estan hecho para leer el archivo que contiene a la sopa
	de letras y transformarla en una lista, devolviendo una tupla con la lista en cuestion y su ancho

	En caso de ser pasado algun argumento, entra en el segundo modo, que sería el de guardar la sopa
	en un archivo llamado sdl.txt para su futuro uso
	"""
	if(n==0):
		archivo=open("sdl.txt", "r")
		sopa=get_lista(archivo)
		lenght = len(sopa[0])
		sopa= plain(get_lista(archivo))
		archivo.close()
		return (sopa,lenght)
	else:
		archivo=open("sdl.txt", "w+")
		for i in range(0,len(tablero[0])):
			if i%tablero[1]==0:
				archivo.write("\n")
				archivo.write(tablero[0][i])
			else:
				archivo.write(tablero[0][i])
		archivo.close()
		linea = open('sdl.txt').readlines()
		with open('sdl.txt', 'w') as f:
			f.writelines(linea[1:])
		archivo.close()



'''	 calc_margen_actual: number->number ->number '''
def calc_margen_actual(ancho_tablero, posicion):
	"""
	Calcula cual es el margen del tablero en la posicion actual.
	Toma el ancho del tablero y la posicion de la primera letra de la palabra.
	"""
	return ((posicion // ancho_tablero)+1)*ancho_tablero

def test_calc_margen_actual():
	assert calc_margen_actual(10,5)==  ((5 // 10)+1)*10
	assert calc_margen_actual(16, 55) == ((55 // 16)+1)*16
	assert calc_margen_actual(18,59) == ((59 // 18)+1)*18

'''sepasa: string->number->number->number ->boolean'''
def sepasa(direccion, posicion, longitud_palabra , ancho_tablero):
	"""
	La función sepasa recibe una dirección (direccion) ("Vertical", "Horizontal", "Diagonal Sup", "Diagonal Inf")
	la posicion inicial de la palabra(posicion) (uno de los lugares de nuestro tablero, que es un numero
	natural), la longitud de la palabra a colocar (longitud_palabra)(un numero natural)
	y el límite de nuestro tablero (margen_tablero)(un numero natural)
	y devuelve un booleano si una palabra con todas esas características (direccion, longitud_palabra y  posicion )
	entra dentro del tablero de la sopa de letras

	Nota: para cada dirección(ori) el programa dispone de tres algoritmos distintos
	"""
	margen = calc_margen_actual(ancho_tablero,posicion)
	if(direccion == "Horizontal"):
		if(posicion + longitud_palabra - 1 > margen):
			return True
	elif(direccion == "Vertical"):
		limite_posicion_vertical = longitud_palabra*ancho_tablero +(posicion - margen)
		if(limite_posicion_vertical > margen or limite_posicion_vertical > ancho_tablero ** 2):
			return True
	elif(direccion == "Diagonal Inf"):
		limite_posicion_diagonal_inf = (posicion + (longitud_palabra-1)*(ancho_tablero+1))
		if(limite_posicion_diagonal_inf > margen or limite_posicion_diagonal_inf > ancho_tablero ** 2):
			return True
	else:
		limite_posicion_diagonal_sup = posicion - (ancho_tablero -1) * longitud_palabra
		if(limite_posicion_diagonal_sup > margen or limite_posicion_diagonal_sup < 0):
			return True
	return False

def test_sepasa():
	assert sepasa("Horizontal", 2, 2, 10) == True
	assert sepasa("Horizontal", 9, 3, 10) == False
	assert sepasa("Vertical", 2, 6 , 10) == True

'''lista lista -> lista'''
def diferencia_simentrica_listas(lista1, lista2):
	"""




	"""

'''lista -> tupla?'''
def cordenadas_palabras(lista_cords_palabras):
	"""






	"""


'''lista -> lista'''
def palabras_encontradas(lista_cords_palabras):
	"""





	"""
	lista_palabras = []
	for elemento in lista_cords_palabras:
		if elemento != []:
			lista_palabras += elemento[0]
	return lista_palabras



'''poner_palabra: string->number->string->list -> list (ori, pos, palabra, tablero)'''
def poner_palabra(direccion, posicion, tablero, palabra,ancho_tablero):
	"""
	La función poner_palabra recibe dirección (ori)("Vertical", "Horizontal", "Diagonal Sup", "Diagonal Inf")
	posicion de inicio (pos)(un numero natural que representa la casilla donde sera colocado el primer carácter 
	de la palabra ingresada), un string (palabra)(la palabra a colocar dentro de la sopa de letras)
	y una lista(tablero)(nuestro tablero de la sopa de letras donde será colocada la palabra ingresada) 
	y devuelve una lista (tablero) modificada que contiene el string (palabra) dentro

	Nota: esta función coloca carácter por carácter en cada una de las posiciones de la lista 
	establecidas por (ori , pos , palabra, y la función sepasa), 
	es decir no coloca el string en una sola posición de la lista(tablero)
	"""
	i=0
	if(direccion=="Horizontal"):
		while i < len(palabra) and posicion + i < calc_margen_actual(ancho_tablero, posicion):
			colision=posicion+i
			if tablero[posicion + i]=="-":
				tablero[posicion+i]=palabra[i]
				i+=1
			elif tablero[posicion + i] == palabra[i]:
				i += 1
			else:
				i=0
				while tablero[posicion + i]!= "-" and posicion + i != colision:
					tablero[posicion + i] = "-"
					i+=1
				
				i=0
				posicion=randint(0, len(tablero)-1)
				while sepasa(direccion,posicion, len(palabra),ancho_tablero):
					 posicion=randint(0, len(tablero)-1)
			
	elif(direccion=="Vertical"):
		while i < len(palabra) and posicion + (i* ancho_tablero)< ancho_tablero**2:
			colision=posicion+(i*ancho_tablero)
			if tablero[posicion + (i* ancho_tablero)]=="-":
				tablero[posicion+(i*ancho_tablero)]=palabra[i]
				i+=1
			elif tablero[posicion+(i*ancho_tablero)] == palabra[i]:
				i += 1
			else:
				i=0
				while tablero[posicion+(i*ancho_tablero)] != "-" and posicion+(i*ancho_tablero) > len(tablero):
					tablero[posicion+(i*ancho_tablero)] = "-"
					i+=1
				
				i=0
				posicion=randint(0, len(tablero)-1)
				while sepasa(direccion,posicion, len(palabra),ancho_tablero):
					 posicion=randint(0, len(tablero)-1)     
		
	elif(direccion=="Diagonal Inf"):
		while i < len(palabra) and\
		posicion + i * (ancho_tablero + 1 )< ancho_tablero**2 +1 and\
		posicion + i * (ancho_tablero + 1 )< calc_margen_actual(ancho_tablero, len(palabra)*posicion):
			colision=posicion + i * (ancho_tablero+ 1 )
			if tablero[posicion + i * (ancho_tablero+ 1 )]=="-":
				tablero[posicion + i * (ancho_tablero + 1 )]=palabra[i]
				i+=1
			elif tablero[posicion + i * (ancho_tablero + 1 )] == palabra[i]:
				i += 1
			else:
				i=0
				while tablero[posicion + i * (ancho_tablero + 1 )] != "-" and posicion + i * (ancho_tablero + 1 ) != colision and posicion + i * (ancho_tablero + 1 ) > len(tablero):
					tablero[posicion + i * (ancho_tablero + 1 )] = "-"
					i+=1
				i=0
				posicion=randint(0, len(tablero)-1)
				while sepasa(direccion,posicion, len(palabra),ancho_tablero):
					 posicion=randint(0, len(tablero)-1)     
	else:
		while i < len(palabra) and\
		posicion - i * (ancho_tablero + 1 )<= calc_margen_actual(ancho_tablero, posicion) and\
		posicion - i * (ancho_tablero + 1 )>0:
			colision=posicion - i * (ancho_tablero + 1 )
			if tablero[posicion - i * (ancho_tablero + 1 )]=="-":
				tablero[posicion - i * (ancho_tablero + 1 )]=palabra[i]
				i+=1
			elif tablero[posicion - i * (ancho_tablero + 1 )] == palabra[i]:
				i += 1
			else:
				i=0
				while tablero[posicion - i * (ancho_tablero - 1 )] != "-" and posicion - i * (ancho_tablero + 1 )< 0 and posicion - i * (ancho_tablero - 1 ) != colision:
					tablero[posicion - i * (ancho_tablero - 1 )] = "-"
					i+=1
				i=0
				posicion=randint(0, len(tablero)-1)
				while sepasa(direccion,posicion, len(palabra),ancho_tablero):
					 posicion=randint(0, len(tablero)-1)
	salida(tablero,ancho_tablero)
	print('\n')   
	return tablero

'''invertir_palabra: string -> string'''
def invertir_palabra(palabra):
	"""
	La función invertir_palabra recibe un string (palabra) y devuelve dicho string al revés
	(esta función será utilizada cuando sea determinado el sentido de la palabra en la función 
	sopa_de_letras o sopa_de_letras_check)
	"""
	return str(palabra[::-1])

def test_invertir_palabra():
	assert invertir_palabra("string") == "gnirts"
	assert invertir_palabra("casa") == "asac"
	assert invertir_palabra("") == ""

'''sopa_de_letras: lista ->lista'''
def sopa_de_letras(lista):
	"""
	La función sopa_de_letras recibe un lista de strings(las palabras que ingreso el usuario) y se encarga de componer nuestra sopa de letras con dichos strings . El funcionamiento de
	esta función básicamente consta de lo siguiente=
	1º Componen nuestro tablero(vacío) a partir de la lista propuesta por el usuario
	2º Toma palabra por palabra y las va colocando dentro del tablero teniendo en cuenta dirección ("Vertical", "Horizontal", "Diagonal Sup", "Diagonal Inf") y sentido("+", "-") (cuando coloca la palabra esta
	esta se elimina de la lista original)
	3º (una vez que la lista ingresada sea vacía) Coloca letras al azar en los lugares que se encuentren vacío del tablero
	4º Muestra el tablero al usuario
	"""
	tablero_original= init_tablero(maximo(lista))
	tablero_sopa=tablero_original[0]
	while lista!=[] :
		direccion = choice(["Vertical","Horizontal","Diagonal Sup","Diagonal Inf"])
		posicion = randint(0, (tablero_original[1]**2)-1)
		ancho_tablero=maximo(lista)
		palabra = choice(lista)
		sentido = choice(["+","-"])

		if(sentido=="-"):
			palabra = invertir_palabra(palabra)

		while sepasa(direccion, posicion, len(palabra), ancho_tablero):
			posicion = randint(0, (tablero_original[1]**2)-1)
			direccion = choice(["Vertical","Horizontal","Diagonal Sup","Diagonal Inf"])
		lista = [elemento for elemento in lista if elemento != palabra]
		tablero_sopa = poner_palabra(direccion, posicion,tablero_sopa,palabra,tablero_original[1])
	
	tablero_sopa = colocar_letras_faltantes(tablero_sopa)

	import_export_sopa((colocar_letras_faltantes(tablero_sopa),tablero_original[1]),1)
	return salida(tablero_sopa,tablero_original[1])

def eleccion(contador1,contador2):
	if contador1 < contador2:
		return "Invertida"
	else:
		return "Normal"
"""
def test_eleccion():
	assert eleccion(1)= "Invertida"
	assert eleccion(1)=
	assert eleccion(1)= 
"""

def generar_cords(palabra,casilla,sentido,direccion):
	lista_cords_palabras=[]
	if direccion == 4:
		lista_cords_palabras += [palabra, casilla, "DiagonalInf", sentido]
	elif direccion == 3:
		lista_cords_palabras += [palabra, casilla, "DiagonalSup", sentido]
	elif direccion == 2:
		lista_cords_palabras += [palabra, casilla, "vertical", sentido]
	elif direccion==1 :
		lista_cords_palabras += [palabra, casilla, "Horizontal", sentido]
	else:
		lista_cords_palabras = []
	return lista_cords_palabras


'''sopa_de_letras_check: list->list ->none'''
def sopa_de_letras_check(sopa_de_letras, lista_de_palabras,ancho_tablero):
	"""
	La funcion sopa_de_letras_check recibe dos listas , la primera es la sopa de letras ya compuesta y la segunda es una liksta de palabras ; y se encarga de ancontrar las palabras de la lista dentro
	de la sopa de letras antes ingresada.	
	Nota= la representacion de la posicion de las palabras dentro de la sopa de letras sera a partir de coordenadas de el primer caracter y el ultimo
	"""
	cont1 = 0
	cont2 = 0
	cont3 = 0
	direccion = 0
	lista_cords_palabras = []
	for palabra in lista_de_palabras:
		for casilla in range(len(sopa_de_letras)):
			while cont1 < len(palabra) or cont2 < len(palabra) or cont3 != len(palabra):
				if palabra[cont1] == sopa_de_letras[casilla + cont1] and  casilla + cont1 <= calc_margen_actual(ancho_tablero):
					cont1 += 1
					direccion = 1
				elif invertir_palabra(palabra)[cont2] == sopa_de_letras[casilla + cont2] and (casilla + cont1 <= calc_margen_actual(ancho_tablero)):
					cont2 += 1
					direccion = 1
				else:
					cont1 = 0
					cont2 = 0
					direccion = 0
					cont3 = len(palabra)
				lista_cords_palabras += generar_cords(palabra, casilla, eleccion(cont1,cont2), direccion)
				cont3 = 0
			while cont1 < len(palabra) or cont2 < len(palabra) or cont3 != len(palabra):
				if palabra[cont1] == sopa_de_letras[casilla + (cont1 * ancho_tablero)] :
					cont1 += 1
					direccion = 2
				elif invertir_palabra(palabra)[cont2] == sopa_de_letras[casilla + (cont2 * ancho_tablero)] :
					cont2 += 1
					direccion = 2
				else:
					cont1 = 0
					cont2 = 0
					direccion = 0
					cont3 = len(palabra)
				lista_cords_palabras += generar_cords(palabra, casilla, eleccion(cont1,cont2), direccion)
				cont3 = 0
			while cont1 < len(palabra) or cont2 < len(palabra) or cont3 != len(palabra):
				if palabra[cont1] == sopa_de_letras[casilla - cont1 * (ancho_tablero + cont1)] :
					cont1 += 1
					direccion = 3
				elif invertir_palabra(palabra)[cont2] == sopa_de_letras[
					casilla - cont2 * (ancho_tablero + cont2)] :
					cont2 += 1
					direccion = 3
				else:
					cont1 = 0
					cont2 = 0
					direccion = 0
					cont3 = len(palabra)
				lista_cords_palabras += generar_cords(palabra, casilla, eleccion(cont1,cont2), direccion)
				cont3 = 0
			while cont1 < len(palabra) or cont2 < len(palabra) or cont3 != len(palabra):
				if palabra[cont1] == sopa_de_letras[casilla + cont1 * (ancho_tablero + cont1)] :
					cont1 += 1
					direccion = 4
				elif invertir_palabra(palabra)[cont2] == sopa_de_letras[
					casilla + cont2 * (ancho_tablero + cont2)] :
					cont2 += 1
					direccion = 4
				else:
					cont1 = 0
					cont2 = 0
					direccion = 0
					cont3 = len(palabra)
				lista_cords_palabras += generar_cords(palabra, casilla, eleccion(cont1,cont2), direccion)
	print(lista_cords_palabras)

#<<<Función Principal>>>

'''main: none -> none'''
def main():
	""" 
	La función main actúa como nuestro menú principal de la sopa de letras, al ser iniciada nos dará la posibilidad de elegir entre tres opciones=

	1. Ingrese lista palabras (al presionar 1)
	2. Ingrese lista de palabras y sopa de letras (al presionar 2)
	3. Salir del programa(al presionar 0)

	si hemos elegido la opción 1 o 2, main nos solicitara una lista de strings o cadenas (“palabras"). Pero en el caso de haber presionado 1 solo se nos mostrara una sopa de letras que en su interior
	posee las cadenas de la lista ingresada anteriormente , y de haber presionado 2 no solo se nos mostrara la sopa de letras sino también la posición de cada una de las cadenas ingresadas.
	"""
	print(
	"""
Se han generado los archivos necesarios para la ejecucion correcta del programa.
Por favor, si esta es su primera vez corriendo el programa, 
elija la opcion salir y rellene los archivos que se encuentran junto al codigo
con los valores necesarios.
-----
De no ser su primera vez ejecutando el archivo, ignore este mensaje, gracias.
<(^_^)/
"""
	)
	wait = input("Presione <ENTER> para continuar")
	print("\n"*40)
	display="MENU\n1.-Ingrese lista palabras\n2Ingrese lista de palabras y sopa de letras\n0.Salir del programa\n*Ingrese una opciòn> "
	menu=int(input(display))
	while menu!=0:
		if menu==1 :
			arc = open("lista_de_palabras.txt","r")
			sopa_de_letras(get_lista(arc))
			arc.close()
			menu=0
		else:
			arc = open("sdl.txt","r")
			lista1= get_lista(arc)
			arc.close
			ancho_de_sopa=len(lista1[0])
			arc = open("lista_de_palabras.txt","r")
			lista2= get_lista(arc)
			arc.close
			sopa_de_letras_check(plain(lista1),lista2,ancho_de_sopa)
			menu=0
	print("Saliendo del programa")

main()



