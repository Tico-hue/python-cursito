# # dato = (input("dame un numero: "))

# """
# def factorial(Numero):
#     if "." in Numero:
#         Numero=float(Numero)
        
        
#     else:
#         Numero=int(Numero)
        
#     if(Numero >= 1):
#         x=1
        
#         while Numero>1:
#             x= x * Numero
#             Numero=Numero-1
#     else:return None     
#     print(x)     
#     return x

# def z(f,h):
#     return f(h)

# def ocho():
#     return '8'
# cientoVeinte = z(factorial,ocho())

    
# print(cientoVeinte)

#Esta función devuelve el factorial del número pasado como parámetro.
# # En caso de que no sea de tipo entero y/o sea menor que 1, debe retornar nulo.
# # Recibe un argumento:
 # numero: Será el número con el que se calcule el factorial
 # Ej:
 # Factorial(4) debe retornar 24
 # Factorial(-2) debe retornar nulo
 # '''
    #Tu código aca:
   


#3) Crear una función que al recibir una lista de números, devuelva el que más se repite y cuántas veces lo hace. 
# Si hay más de un "más repetido", que devuelva cualquiera

# lucha
# def calcular_el_max(lista):
#     contadores={}
    
#     for numero in lista:
#         if numero in contadores:
#             contadores[numero] += 1 
#         else: contadores[numero]=1
    
#     mayor=0
#     numero_rep_max=0
    
#     for clave in contadores:
#       if mayor < contadores[clave]:
#           mayor = contadores[clave]
#           numero_rep_max= clave

# anita
# def calcular_el_max(lista):
#     contadores={}
#     maximo=0
#     claveDelMaximo=0
#     for numero in lista:
#         if numero in contadores:
#             contadores[numero] += 1 
#         else: contadores[numero]=1
#         maximo= dameElMax(contadores[numero],maximo)
#         claveDelMaximo=numero
  
       
#     print(maximo, claveDelMaximo)

# def dameElMax(n1,n2):
#     if n1>n2:
#         return n1
#     return n2
    
# calcular_el_max([1,1,1,1,5,5,8,8,9,"luciano","luciano","luciano","luciano","luciano","luciano"])


#contadores en la posicion clave es igual a la frecuencia 
#por ej: con la clave = 5 la frecuencia es 2


# mayor = 0
# # for numero in lista:
# #     if numero > mayor:
# #         mayor = numero

# In[33]:

#4) ahora hacerlo recursiva

#5)1. Write a Python function to find the maximum of three numbers.

# def maximoDeTres(n1,n2,n3):
#     mayordeTodos=n1
#     if n1<n2:
#         mayordeTodos= n2
#     if mayordeTodos<n3:
#         mayordeTodos=n3
#     return mayordeTodos

# print(maximoDeTres(1113132133,84884,16611661))
    
# def maximoDeTres(n1, n2, n3):
#     mayordeTodos = n1 if n1 > n2 else n2
#     mayordeTodos = n3 if n3 > mayordeTodos else mayordeTodos
#     return mayordeTodos

# print(maximoDeTres(654,8,99))


#7. Write a Python function that accepts a string and counts the number of upper and lower case letters.

# escribir una fucnion que reciba un string y devuelva si es o no un palindromo

# def isPalind....

# anitalagordalagarton anotragaladrogalatina
# oso="osobaboso12"

#txt = "oso oso" [::-1]
# def esunPalindromo(fraseDudosa):
#     cantidadCaracteres=len(fraseDudosa)
#     if cantidadCaracteres%2==0:
#         fraseDudosa.split
# frase="anitalagordalagartonanotragaladrogalatina"

# def esunPalindromo(frase):
#     fraseInvertida=frase[::-1]
#     return fraseInvertida == frase

# print(esunPalindromo("osobssdboso"))
# 0.
# nota: 10/10
# ahora hacerlo sin [::-1]

def calcularEseNumerazo(numerazo=0,cont=0):
    if cont < 33:
        numerazo += 2**cont
        cont+= 1
        numerazo= calcularEseNumerazo(numerazo,cont)
    return numerazo

print(calcularEseNumerazo())


def factorial(n,fact=1):
    if n > 1:
        fact *= n
        n-=1
        fact = factorial(n,fact) 
    return fact
print(factorial(5))