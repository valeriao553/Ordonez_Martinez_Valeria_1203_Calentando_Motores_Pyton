print(" ")
print("Ordonez Martinez Valeria")
print(" ")
def inversa(a):
    # Función para invertir la cadena
    return a[::-1]
#Definir funcion
def isPalindromo(a):
    # Comprobar si la cadena es igual a su inversa
    inv = inversa(a)
    if inv == a:
        return True
    else:
        return False

# imprimir
print(isPalindromo("radar"))  # True
print(" ")

