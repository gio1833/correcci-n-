def es_palindromo(texto):# se le agrega los dos puntos al final para que la sintaxis pueda continar y asi no tener errorer
    texto = ''.join(caracter.lower() for caracter in texto if caracter.isalnum())
    return texto == texto[::-1]

palabra_frase = input("Ingrese una palabra o frase: ")
if es_palindromo(palabra_frase):# se le agrega a la variable la funcion para el polindromo
    print(f"{palabra_frase} es un palíndromo.")
else:
    print(f"{palabra_frase} no es un palíndromo.")
