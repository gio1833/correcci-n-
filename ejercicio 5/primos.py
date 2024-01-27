def es_primo(numero): # se corregio porque le faltaba los dos puntos 
    if numero < 2: # se define la variable numero 
        return False
    for i in range(2, int(numero**0.5) + 1):
        if numero % i == 0:
            return False # se corregi return en la linea estaba mal escrito 
    return True # se corregi return en la linea estaba mal escrito 

limite = int(input("Ingrese el límite superior para encontrar números primos: "))
primos = [num for num in range(2, limite + 1) if es_primo(num)]# se agrega num en la funcion
print("Números primos:", primos)
