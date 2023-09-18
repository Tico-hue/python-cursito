#!/usr/bin/env python
# coding: utf-8

# ## Variables

# 1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
a= 4
b= 2
c= a+b
print(c)

# In[7]:


variable1= 14

# print(variable1)

# 2) Imprimir el tipo de dato de la constante 8.5

# In[3]:

variable2= 8.5

# print(type(variable2))





# 3) Imprimir el tipo de dato de la variable creada en el punto 1

# In[8]:
# print(type(variable1))




# 4) Crear una variable que contenga tu nombre

# In[2]:
mi_nombre="anita"



# 5) Crear una variable que contenga un número complejo

# In[3]:

variable_numero_complejo=complex(4,-5)



# 6) Mostrar el tipo de dato de la variable crada en el punto 5

# In[4]:

# print(variable_numero_complejo)



# 7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales

# In[1]:


pi = 3.1416


# 8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?

# In[3]:

variable_true= "true"
variable_verdadera= True



# 9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8

# In[5]:

# print(type(variable_true))

# print(type(variable_verdadera))


# 10) Asignar a una variable, la suma de un número entero y otro decimal

# In[1]:

suma= 4+2.1

# print(suma)



# 11) Realizar una operación de suma de números complejos

# In[2]:

suma_complejos= complex(5,-8)+complex(6,-1)

# print(suma_complejos)

# 12) Realizar una operación de suma de un número real y otro complejo

# In[4]:
suma_complejos= 5.4 +complex(6,-1)

# print(suma_complejos)





# 13) Realizar una operación de multiplicación

# In[5]:

multiplicacion= 5*5
# print(multiplicacion)



# 14) Mostrar el resultado de elevar 2 a la octava potencia

# In[6]:

potencia=2**8
# print(potencia)

# 15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla

# In[8]:

division= 27/4

# print(division)



# 16) De la división anterior solamente mostrar la parte entera

# In[9]:

# print(int(division))



# 17) De la división de 27 entre 4 mostrar solamente el resto

# In[1]:

# print(27%4)

resto= 27%4

# 18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado

# In[2]:
# print(int(division)*4+resto)




# 19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas

# In[3]:
palabra="12"

# print(palabra+palabra)




# 20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?

# In[4]:
# print(2==int("2"))




# 21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera

# In[11]:





# 22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')

# In[12]:


a = float('3.8')


# 23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido y que de como resultado 2.

# In[15]:

a=3
a-= 1
a =a-1
# print(a)



# 24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?

# In[29]:
1 << 2





# 25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?

# In[23]:






# 26) Realizar una operación válida entre valores de tipo entero y string

# In[30]:

# print(4*"hora")