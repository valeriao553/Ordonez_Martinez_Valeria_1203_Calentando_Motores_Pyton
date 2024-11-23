print(" ")
print("Ordonez Martinez Valeria")
print(" ")
#Definimos funcion
def suma(a):
    total = 0
#Crear bucle for
    for i in range(len(a)):
        total += a[i] 
#Devolver valor
    return total
#Definir funcion
def mult(a):
    total = 1
    for i in range(len(a)):
        total *= a[i]
#Devolver valor
    return total
#Mostrar resultados
print(suma([1,2,3,4]))
print(mult([1,2,3,4]))
print(" ")