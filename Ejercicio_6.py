print(" ")
print("Ordonez Martinez Valeria")
print(" ")
#Definimos funcion
def inversa(a):
    # Verifica si la entrada es un número
    if isinstance(a, (int, float)):  
        print("La entrada es un número")
        return "Error"
    
    # Verifica si la entrada es un único carácter
    if isinstance(a, str) and len(a) == 1:
        print("La entrada no debe ser un número o una sola letra")
        return "Error"
    
    # Invierte la cadena si es válida
    if isinstance(a, str):
        return a[::-1]  # Usamos slicing para invertir
    
    # Si la entrada no es válida
    print("Entrada no válida")
    return "Error"

# Imprimir de la manera correcta
print(inversa("odnaborp yotse"))  
print(" ")
