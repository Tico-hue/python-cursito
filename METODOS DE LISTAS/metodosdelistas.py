# LIST:
# #esto es crear una lista con list()

lista = list(["Hola","lucha", 45])
print(lista)


# lend:
#esto devuelve la cantidad de elementos de una lista
len
cantidad_elementos = len(lista)
print(cantidad_elementos)

#todo esto agrega elementos a una lista:

#APPEND: agrega un elemento a la lista

lista.append("coscu")
print(lista)

#INSERT: inserta un elemento en la posicion que desees de la lista

lista.insert(2,"gil")
print(lista)

#EXTEND: agrega varios elementos a la lista

lista.extend(["terere", 4558])
print(lista)


# POP:
#ESTO ES PARA ELIMINAR ELEMENTOS DE UNA LISTA DE LA POSICION QUE DESEES

lista.pop(0)
print(lista)

# REMOVE:
#CON ESTO ELIMINAMOS UN ELEMENTO DE LA LISTA POR SU VALOR

lista.remove("coscu")
print(lista)

# CLEAR: CON ESTO ELIMINAS TODOS LOS ELEMENTOS DE UNA LISTA

#lista.clear()
print(lista)

#SORT : ESTO ORDENA LOS ELEMENTOS DE UNA LISTA EN ORDEN ASCENDENTE. 

#lista.sort()
print(lista)
# NO FUNCIONA SI LA Lista tiene cadenas de texto

Nueva_lista= [0, 56, 86, 41, 16, 8, 14, 5]
Nueva_lista.sort()
Nueva_lista.reverse()
print(Nueva_lista)

#REVERSE SE USA PARA INVERTIR UNA LISTA.

 