import itertools
# Definimos las variables
variables = ['A', 'B']
# Generamos todas las combinaciones de valores booleanos
combinaciones = list(itertools.product([True, False], repeat=len(variables)))
# Imprimimos la cabecera de la tabla
print(f"{' | '.join(variables)} | A AND B")
print("-" * 30)
# Evaluamos la expresión para cada combinación
for combinacion in combinaciones:
    A, B = combinacion
    resultado = A and B
    print(f"{A} | {B} | {resultado}")