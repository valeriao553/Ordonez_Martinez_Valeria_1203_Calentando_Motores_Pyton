print(" ")
print("Ordonez Martinez Valeria")
print(" ")
#Definir funcion
def isnum(a):
    try:
        int(a)
    except:
        return False;
    return True;
#Definir funcion
def length(a):
    i = 0
    #Crear condiciones
    if not (isnum(a)):
        #Usar rango
        for i in range(len(a)):
            i = i + 1
    elif(isnum(a)):
        #Devolver valores
        return(a)
    return(i)
#Imprimir valores
print(length("Valeria"))
print(length(["1","2","3"]))
print(" ")
