def cajero():
    print("Bienvenido al cajero")
    saldo = 1000
    #Bucle para conocer las opciones del cajero 
    while True:
        print("1. Ingresar dinero")
        print("2. Retirar dinero")
        print("3. Ver saldo")
        print("4. Salir")
        opcion = input("¿Qué deseas hacer? ")
        #Opcion 1: para ingresar dinero
        if opcion == "1":
            monto = float(input("¿Cuánto dinero deseas ingresar? $"))
            saldo += monto
            print(f"Se ha ingresado ${monto} a tu cuenta. Tu saldo actual es ${saldo}")
        #Opcion 2: para retirar dinero
        elif opcion == "2":
            monto = float(input("¿Cuánto dinero deseas retirar? $"))
            if monto <= saldo:
                saldo -= monto
            print(f"Se ha retirado ${monto} de tu cuenta. Tu saldo actual es ${saldo}")
        #Opcion 3: para ver el saldo
        elif opcion == "3":
            print(f"Tu saldo actual es ${saldo}")
        #Opcion 4: para salir
        elif opcion == "4":
            print("Gracias por utilizar el cajero")
            break
        else:
            print("Opción no válida. Por favor, intenta de nuevo.")
            
cajero()  
        