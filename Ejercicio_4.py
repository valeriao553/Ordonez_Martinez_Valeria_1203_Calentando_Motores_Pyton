print(" ")
print("Ordonez Martinez Valeria")
print(" ")

def isvoc(s):
    vocales = "aeiouáéíóú"
    # Verifica si es un solo carácter y si es una vocal
    return isinstance(s, str) and len(s) == 1 and s.lower() in vocales

# Ejemplos de letras
print(isvoc("a"))  
print(isvoc("b"))  
print(isvoc("á"))  
print(isvoc("as")) 
print(isvoc(1))    
print(" ")

