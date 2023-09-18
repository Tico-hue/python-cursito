def calcularEdad(fecha_actual, fecha_nacimiento):
    
    diaActual=  int(fecha_actual.split("/")[0])
    mesActual=  int(fecha_actual.split("/")[1])
    anioActual=  int(fecha_actual.split("/")[2])
    diaNacimiento=  int(fecha_nacimiento.split("/")[0])
    mesNacimiento=  int(fecha_nacimiento.split("/")[1])
    anioNacimiento=  int(fecha_nacimiento.split("/")[2])
    
    edad=0
    
    if mesActual > mesNacimiento:
        edad=anioActual-anioNacimiento

    elif mesActual==mesNacimiento:
        if diaActual>diaNacimiento:
            edad=anioActual-anioNacimiento
           
        else:
            edad=anioActual-anioNacimiento
            edad=edad-1
        if diaActual==diaNacimiento:
            edad=edad+1 
    else: 
        edad=anioActual-anioNacimiento
        edad= edad-1
    
    
        
    
    print(edad)
    
    
calcularEdad("15/08/2023", "14/07/1996")    