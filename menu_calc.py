# El bucle while permite que el programa ejecute continuamente.
# Finaliza cuando el usuario lo indique 
while   True:
    # Mostrar un menú de la calculadora.
    print("\n========MENÚ CALCULADORA========")
    print("1. Suma")
    print("2. Resta")
    print("3. Salir")

    # Se solicita al usuario que elija una opción del menú
    opcion = input("Elija una opción (1-3): ")

    # Opción 1: Suma

    if opcion == "1":
        num1 =float(input("Ingrese el primer número: "))
        num2 =float(input("Ingrese el sengundo número: "))

        # calcular la suma
        resultado = num1+num2
        # Mostrar resultado
        print(f"El resultado es: {resultado}")

    # Opción 2: Resta
    elif opcion == "2":
        num1 =float(input("Ingrese el primer número: "))
        num2 =float(input("Ingrese el sengundo número: "))

        # calcular la resta
        resultado = num1+num2
        # Mostrar resultado
        print(f"El resultado es: {resultado}")
    
    # Opción 3: Salir del programa
    elif opcion == "3":
        # Mensaje de cierre
        break # Termina el bucle while
    
    # Opcion inválida
    else: 
        print("Opción invalida. Por favor, seleccione una opcion del 1 al 3.")
    
    input("Presione enter para continuar...")
    



    