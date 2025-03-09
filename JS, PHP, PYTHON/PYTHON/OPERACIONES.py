num1 = 10
num2 = 5

def suma():
    sum = num1 + num2
    print("Resultado de la suma:", sum)
suma()

def resta():
    rest = num1 - num2
    print("Resultado de la resta:", rest)
resta()
    
def multiplicacion():
    mult = num1 * num2
    print("Resultado de la multiplicacion:", mult)
multiplicacion()

def division():
    if num2 != 0:
        div = num1 / num2
        print("Resultado de la division:", div)
    else:
        print("No se puede dividir entre cero")
division()
        
def potencia():
    pot = num1 ** num2
    print("Resultado de la potencia:", pot)
potencia()  