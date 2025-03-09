def tabla():
    while True:
        try:
            num = int(input("Ingrese un numero para conocer la tabla de multiplicar: "))
            for i in range (1, 11):
                print(f"{num} x {i} = {num * i}")
        except:
            print("Error, por favor ingrese un numero entero")
            
tabla()