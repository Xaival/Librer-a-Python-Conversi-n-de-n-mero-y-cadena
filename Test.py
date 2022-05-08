from ConvertDicc import NumDiccionario
from ConvertDicc import DiccionarioNum
from ConvertDicc import DiccionarioPreder

# Convertir numérico en lista caracteres
Diccionario = ["A", "B", "C"] # Array
Devolver = [0, 4] # Devolver del 0 al 27
Grupo = 5 # Devolver con 5 caracteres
print(NumDiccionario(Diccionario, Devolver, Grupo))
# ['AAAAA', 'AAAAB', 'AAAAC', 'AAABA', 'AAABB']


# Convertir lista a numérico
Diccionario = ["A", "B", "C"] # Diccionario de elementos
Resolver = ['AAAAA', 'AAAAC', 'AACAB'] # Elementos para resolver
print(DiccionarioNum(Diccionario, Resolver))
# [0, 2, 19]


# Llamar librería predeterminada
print(DiccionarioPredeter("AZ"))
# ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
