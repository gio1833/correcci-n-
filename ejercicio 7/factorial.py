def factorial(n):# se corrige y se agregan los dos puntos para que la funcion se ejecute
    if n == 0 or n == 1: # se agrega un (=) para que sea valida la comparacion y asi poder ejecutar la variable
        return 1
    else:
        return n * factorial(n - 1)

numero = int(input("Ingrese un número para calcular su factorial: "))
print(f"El factorial de {numero} es {factorial(numero)}") # se agrega la palabra numero para la funcion de la variable
