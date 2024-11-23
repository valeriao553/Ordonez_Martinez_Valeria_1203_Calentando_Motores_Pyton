print(" ")
print(" Ordonez Martinez Valeria")
print(" ")
#Definir funcion
def histograma(lista):
    #Creamos bucle for
    for numero in lista:
        #Condiciones
        if isinstance(numero, int) and numero >= 0:  # Verifica que sea un entero no negativo
            print('*' * numero)
        else:
            print("Entrada inválida:", numero)

# Imprimimos
histograma([4, 9, 7])
print(" ")

