#!/usr/bin/env python
# coding: utf-8

# ## Flujos de Control

# 1) Crear una variable que contenga un elemento del conjunto de números enteros 
# y luego imprimir por pantalla si es mayor o menor a cero

# In[4]:
# a=5

# print(a>0)
# print(a<0)
# print(a>=0)


# 2) Crear dos variables y un condicional que informe si son del mismo tipo de dato

# In[5]:
# print(type(None))

# a = 'es un string jeje'
# b = 9
# c = 'asd'

# if type('s') == type(c):
#     print('ecole')
# else:
#     print('na q ve')

# 3) Para los valores enteros del 1 al 20, imprimir por pantalla si es par o impar
# In[7]:

# cont=1

# while cont<20:
#     if cont%2==0:
#     cont+=1
#         print("par",cont)
#     else:
#         print("impar",cont)
    
    
# 4) En un ciclo for mostrar para los valores entre 0 y 5 el resultado de elevarlo a la potencia igual a 3

# In[9]:

# for x in range(6):
#     print(x**3)




# 5) Crear una variable que contenga un número entero y realizar un ciclo for la misma cantidad de ciclos

# In[10]:

# z=8
#  for s in range(z):
   #   print(s)



# 6) Utilizar un ciclo while para realizar el factoreo de un número guardado en una variable, sólo si la variable contiene un número entero mayor a 0

# In[33]:
# # a=8
# r=1
# while a>0:
#    r*=a
#    a=a-1

# print(r)

# 7) Crear un ciclo for dentro de un ciclo while

# In[38]:





# 8) Crear un ciclo while dentro de un ciclo for

# In[3]:





# 9) Imprimir los números primos existentes entre 0 y 30

# In[54]:

# 9.a) RECORRER UNA LISTA DE NUMEROS E IMPRIMIR EL MAYOR

# # lista = [2, 3, 4, 86, 66, 7, 8, 834, 34, 1000, 2000, 2500, 8000]
# # mayor = lista.sort()
# # for numero in lista:
# #     if numero > mayor:
# #         mayor = numero

# print("El número mayor es:", mayor)


# 9.b) a partir de un numero imprimir si es primo o no
# z=98
# r=0
# for s in range(1,z+1):

#    if  z%s==0:
#       r=r+1
#    if r>2: break
#    print(s)  
# if r==2:
#    print(z,"es primo")
# else: print(z, "no es primo")    

#9.c) determinar edad

diaActual=9
mesActual=7
añoActual=2023

diaNacimiento=10
mesNacimiento=7
añoNacimiento=1998

edad=añoActual-añoNacimiento

if mesActual>mesNacimiento :
   print(edad)
elif mesActual==mesNacimiento:
   if diaActual>=diaNacimiento:
      print("tenes", edad)
   else:
      print(edad-1)
else: 
   edad=edad-1
   print("tenes", edad)


   
# 10) ¿Se puede mejorar el proceso del punto 9? Utilizar las sentencias break y/ó continue para tal fin

# In[55]:





# 11) En los puntos 9 y 10, se diseño un código que encuentra números primos y además se lo optimizó. ¿Es posible saber en qué medida se optimizó?

# In[56]:




# In[57]:




# 12) Si la cantidad de números que se evalúa es mayor a treinta, esa optimización crece?

# In[58]:





# In[59]:




# 13) Aplicando continue, armar un ciclo while que solo imprima los valores divisibles por 12, dentro del rango de números de 100 a 300

# In[62]:





# 14) Utilizar la función **input()** que permite hacer ingresos por teclado, para encontrar números primos y dar la opción al usario de buscar el siguiente

# In[73]:




# 15) Crear un ciclo while que encuentre dentro del rango de 100 a 300 el primer número divisible por 3 y además múltiplo de 6

# In[75]: