ingreso_mensual=int(input("ingresa tu soldi mensual"))
gasto_mensual=int(input("ingresa tu gasto mensual"))
 
if ingreso_mensual >= 1000: 
     if ingreso_mensual-gasto_mensual <= 30: 
         print("tenes que ahorrar")
     elif ingreso_mensual- gasto_mensual <= 200: 
         print("tenes ahorros")
     else:
         print("va bene")
     
elif ingreso_mensual > 500:
    print("ganas justo")

elif ingreso_mensual > 200:
    print("ganas justo para venezuela")

else:
    print("ganas poco")
    
print ("te queda para ahorrar: ", ingreso_mensual-gasto_mensual)