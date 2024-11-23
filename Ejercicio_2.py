print(" ")
print("Ordonez Martinez Valeria")
print(" ")
#Definir funcion
def mayor3(a,b,c):
    #Agregar condiciones
    if((a > b) and (a > c)):
        #Devolver resultado
        return a
    if((b > a) and (b > c)):
        #Devolver resultado
        return b
    if((c > a) and (c > b)):
        #Devolver resultado
        return c
#Imprimir
print("El numero mayor es:" ,mayor3(18,17,20))
print(" ")