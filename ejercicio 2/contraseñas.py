import random # se modifica random no esta bien llamado en funcion
import string

def generar_contraseña(longitud=8): # se llama def para llamar la fincion
    caracteres = string.ascii_letters + string.digits + string.punctuation
    contraseña = ''.join(random.choice(caracteres) for _ in range(longitud))
    return contraseña

print(generar_contraseña()) # se corregi el palabra contaraseña la n
