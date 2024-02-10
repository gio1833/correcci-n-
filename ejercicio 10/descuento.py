def calcular_precio_con_descuento(precio_base, porcentaje_descuento): # se corregi la parabra descuento y se le añade a la funcion def
    descuento = precio_base * (porcentaje_descuento / 100)
    precio_final = precio_base - descuento
    return precio_final # se corregi return

precio_base = float (input("Ingrese el precio base del producto: ")) # se corrige el input
porcentaje_descuento = float(input("Ingrese el porcentaje de descuento: "))
precio_final = calcular_precio_con_descuento(precio_base, porcentaje_descuento)
print(f"El precio final con {porcentaje_descuento}% de descuento es: {precio_final}")
