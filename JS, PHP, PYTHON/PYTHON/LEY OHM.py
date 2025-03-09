def calcularLeyOhm():
    print("Calculadora de la Ley de Ohm")
    print("Selecciona la variable que deseas calcular:")
    print("1. Voltaje (V)")
    print("2. Corriente (I)")
    print("3. Resistencia (R)")

    opcion = input("Ingresa el número de la opción (1, 2 o 3): ")

    if opcion == '1':
        I = float(input("Ingresa la corriente (I) en amperios: "))
        R = float(input("Ingresa la resistencia (R) en ohmios: "))
        V = I * R
        print(f"El voltaje (V) es: {V} voltios")

    elif opcion == '2':
        V = float(input("Ingresa el voltaje (V) en voltios: "))
        R = float(input("Ingresa la resistencia (R) en ohmios: "))
        I = V / R
        print(f"La corriente (I) es: {I} amperios")

    elif opcion == '3':
        V = float(input("Ingresa el voltaje (V) en voltios: "))
        I = float(input("Ingresa la corriente (I) en amperios: "))
        R = V / I
        print(f"La resistencia (R) es: {R} ohmios")

    else:
        print("Opción no válida. Por favor, selecciona 1, 2 o 3.")

calcularLeyOhm()