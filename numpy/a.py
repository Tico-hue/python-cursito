import numpy as np
# lista=[0,1,2,3,4]
arr=np.array(list)
# # matriz=[1,2,3],[5,6,7],[8,9,10]
# # matriz=np.array(matriz)
# # print(arr[::3])

# # print(matriz[1:,0:2])

# #tipos de datos
# arr=np.array(lista, dtype="float64")
# print(arr.dtype)
# arr=arr.astype(np.string_)

# print(arr)


#dimensiones de datos
# vector=np.array([1,2,3])
# print(vector)
# print(vector.ndim)


# matriz=np.array([[1,2,3],[4,5,6]])
# print(matriz)
# print(matriz.ndim)

# tensor=np.array([[[1,2,3],[4,5,6],[40,55,9]],[[1,2,3],[4,5,6],[40,55,9]]] )
# print(tensor)
# print(tensor.ndim)

# #agregar dimensiones o eliminar
# import numpy as np

# vector = np.array([[[[[[[[[[1, 2, 3]]]]]]]]]])
# print(vector)
# print(vector.ndim)

# expand=np.expand_dims(vector,axis=0)

# print(expand)

# achicar=np.squeeze(vector)

# print(achicar,achicar.ndim)

#creando arrays



# print(np.arange(0,10))

# print(np.zeros((10,10)))
# print(np.ones((10,10)))

# print(np.linspace(1,14,20))

# print(np.eye(4))

# print(np.random.rand(5,5))

# print(np.random.randint(1, 100, (10,10)))

#shape y reshape

formita=np.random.randint(1,10,(3,2))
formita2=np.array([2,10])

#print(formita)

reshaped_formita2=np.reshape(formita2(2,1),"c")

print(reshaped_formita2)