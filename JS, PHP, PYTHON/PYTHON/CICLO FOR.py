def inversion():
    cant = float(input("Ingrese la cantidad a invertir: $"))
    inter = float(input("Ingrese el interés anual: "))
    años = int(input("Ingrese el número de años: "))
    
    for i in range(años):
        cant = cant + (cant * (inter / 100))
        print(f"En un año tu capital obtenido sera: ${cant:.2f}")
        
inversion()
        