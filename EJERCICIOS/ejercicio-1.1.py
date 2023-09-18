#1) DIFERENCIAR EN PORCENTAJE ENTRE ESTE CURSO Y : 
# - EL MAS RAPIDO DE OTROS CURSOS 
# - EL MAS LENTO DE OTROS CURSOS
# - EL PROMEDIO DE CURSOS 

#Duraciones de cursos: HORAS

Curso_de_Dalto = 1.5
Otro_Curso_min = 2.5  
Otro_Curso_Max = 7
Cursos_Promedio = 4

Diferencia_con_min = 100 - Curso_de_Dalto / Otro_Curso_min * 100
print(f"el curso de dalto es {Diferencia_con_min}% mas rapido que el mas rapido")

Diferencia_con_max = 100 - Curso_de_Dalto / Otro_Curso_Max * 100
print(f"el curso de dalto es {Diferencia_con_max}% mas rapido que el mas lento")


Cursos_Promedio = 100 - Curso_de_Dalto /  Cursos_Promedio * 100
print(f"el curso de dalto es {Cursos_Promedio}% mas rapido que el promedio")

