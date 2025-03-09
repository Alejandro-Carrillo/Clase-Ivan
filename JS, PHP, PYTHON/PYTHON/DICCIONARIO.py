diccionario = {'Euro':'€', 'Dollar':'$', 'Yen':'¥', 'Peso':'$'}

peso = diccionario

def conversor():
    divisa = input("Ingrese el tipo de divisa: ").capitalize()  
    if divisa in peso:
        print("Esta es la divisa:", peso[divisa])
    else:
        print("Divisa no encontrada.")
        
conversor()
