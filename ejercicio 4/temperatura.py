def celsius_a_fahrenheit(celsius):# se agregan en la def los dos puntos 
    return (celsius * 9/5)  + 32 # en la linea se le agrega el signo + para que la variable 

temperatura_celsius = float (input("Ingrese la temperatura en Celsius: ")) # se le agreaga input en la variable
temperatura_fahrenheit = celsius_a_fahrenheit(temperatura_celsius)
print(f"{temperatura_celsius}°C es igual a {temperatura_fahrenheit}°F")
