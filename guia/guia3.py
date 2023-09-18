#!/usr/bin/env python
# coding: utf-8

# ## Estructuras de Datos

# 1) Crear una lista que contenga nombres de ciudades del mundo que contenga más de 5 elementos e imprimir por pantalla

# In[3]:

lis = ['Buenos Aires','Brasilia','Asunción','Montevideo','Santiago','Lima','Caracas','Bogotá']




# 2) Imprimir por pantalla el segundo elemento de la lista

# In[4]:

# print(lis[1])


# 3) Imprimir por pantalla del segundo al cuarto elemento

# In[8]:

# for x in range(len(lis)):
#     if x >= 1 and x < 5:
#         print(lis[x]) 




# 4) Visualizar el tipo de dato de la lista

# In[12]:
#print(type(lis))




# 5) Visualizar todos los elementos de la lista a partir del tercero de manera genérica, es decir, sin explicitar la posición del último elemento

# In[14]:

#print(lis[2:len(lis)])



# 6) Visualizar los primeros 4 elementos de la lista

# In[15]:
#print(lis[:4])


    


# 7) Agregar una ciudad más a la lista que ya exista y otra que no ¿Arroja algún tipo de error?

# In[16]:

# lis.append("rende")
# lis.append("Montevideo")
# print(lis)







# 8) Agregar otra ciudad, pero en la cuarta posición

# In[20]:

# lis.insert(3,"cosenza")
# print(lis)


# In[21]:




# 9) Concatenar otra lista a la ya creada

# In[22]:
# lista=["cordoba", "pisa", "andorra"]

# lis.extend(lista)
# print(lis)


# 10) Encontrar el índice de la ciudad que en el punto 7 agregamos duplicada. ¿Se nota alguna particularidad?

# In[23]:





# 11) ¿Qué pasa si se busca un elemento que no existe?

# In[24]:

#lis.index("cba")



# 12) Eliminar un elemento de la lista

# In[25]:

# lis.remove("cordoba")
# print(lis)



# 13) ¿Qué pasa si el elemento a eliminar no existe?

# In[27]:

# lis.remove("3")
# print(lis)


# 14) Extraer el úlimo elemento de la lista, guardarlo en una variable e imprimirlo

# In[28]:
# ultimo_elemento = lis.pop(-1)

# print(ultimo_elemento)


# 15) Mostrar la lista multiplicada por 4

# In[29]:
# print(lis*4)


# # 16) Crear una tupla que contenga los números enteros del 1 al 20

# # In[32]:
tuplis=(1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20,20,20)


# # 17) Imprimir desde el índice 10 al 15 de la tupla

# # In[35]:

# print(tuplis[9:15])


# 18) Evaluar si los números 20 y 30 están dentro de la tupla

# In[41]:

# if 30 in tuplis:
#     print("si")
# else: print("no30")

# if 20 in tuplis:
#     print("si20")
# else: print("no")

# 19) Con la lista creada en el punto 1, validar la existencia del elemento 'París' y si no existe, agregarlo. Utilizar una variable e informar lo sucedido.

# In[#
# elemento_paris= "paris"

# if elemento_paris in lis:
#     print("esta")
# else: print("no esta")



# 20) Mostrar la cantidad de veces que se encuentra un elemento específico dentro de la tupla y de la lista

# In[51]:

# elemento_tupla=20

# cantidad=tuplis.count(elemento_tupla)

# print(elemento_tupla, "esta" , cantidad, "veces en la tupla" )

# cantidad_en_lista=lis.count(elemento_tupla)
# print(elemento_tupla, "esta" , cantidad_en_lista, "veces en la lista" )

# 21) Convertir la tupla en una lista

# In[52]:

ahora_es_tupla=tuple(lis)

print(ahora_es_tupla)

def toTupla(unaLista):
    return tuple(unaLista)

tuplaNueva= toTupla(lis)

print(tuplaNueva)
# 22) Desempaquetar solo los primeros 3 elementos de la tupla en 3 variables

# In[55]:

def desempaquetar(unaTupla):
    b=unaTupla[1]
    c=unaTupla[2]
    a=unaTupla[0]
    print(a,b,c)
    #return(a,b,c)

llamado_de_elementos=desempaquetar((7,8,5,44,6,7))

print(llamado_de_elementos)
    
    
    



# 23) Crear un diccionario utilizando la lista crada en el punto 1, 
# asignandole la clave "ciudad". Agregar tambien otras claves,
# como puede ser "Pais" y "Continente".

# In[57]:
lis = ['Buenos Aires','Brasilia','Asunción','Montevideo','Santiago','Lima','Caracas','Bogotá']
def xd(list):
    nuevaList=[]
    for i in range(len(list)):
        list[i]={"ciudad":list[i]}
        #nuevaList.append({"ciudad":city})
    return list
print(lis)
xd(lis)
print(lis)
        
        




# 24) Imprimir las claves del diccionario

# In[59]:




# 25) Imprimir las ciudades a través de su clave

# In[61]:




Posiciones=0
Auxiliar=0
ContadorVueltas=0
Apuntador1=1
Apuntador2=2
lista= []
Posiciones=int(input('cuantos numeros deseas ordenar'))



lucha={"nombre": "luciano",
 "edad": 26,
 "nacionalidad": "argentina"}

