def contar_palabra(texto, palabra):# se agrega en la definicion los dos puntos
    return texto.lower().split().count(palabra.lower())

texto = "Este es un ejemplo de texto. Este texto tiene palabras repetidas."
palabra_buscada = "texto"

print(f"La palabra '{palabra_buscada} aparece {contar_palabra(texto, palabra_buscada)} veces.")# se le agregan las llaves en las palabra buscada y en contar palabra
