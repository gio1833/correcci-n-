def calculadora():
    num1 = float(input("Ingrese el primer número:"))
    num2 = float(input("Ingrese el segundo número:"))
    operacion = input("Ingrese la operación (+, -, *, /): ")

    if operacion == '+':
        resultado = num1 + num2 # correc 
    elif operacion == '-':
        resultado = num1 - num2
    elif operacion == '*':
        resultado = num1 * num2
    elif operacion == '/':
        resultado = num1 / num2 # correc
    else:
        resultado = "Operación no válida"
    
    print("Resultado: ",resultado) # correc

calculadora()
