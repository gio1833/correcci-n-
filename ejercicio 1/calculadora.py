def calculadora():
    num1 = float(input("Ingrese el primer número:")) # convertir esa entrada y luego almacenarlo en la variable
    num2 = float(input("Ingrese el segundo número:"))# convertir esa entrada y luego almacenarlo en la variable
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num1 + num2 # se difiene num como varibale num1
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2 # se difine num como variable num1
    else:
        resultado = "Operación no válida"
    
    print("Resultado: ",resultado) # se coloca coma despues de cerrar comillas

calculadora()
