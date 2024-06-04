def identificar_cuadrilatero(lados):
    # Desempaquetamos las longitudes de los lados
    a, b, c, d = lados
    
    # Comprobamos si todos los lados son iguales
    if a == b == c == d:
        return "Cuadrado"
    
    # Comprobamos si hay dos pares de lados iguales
    elif (a == c and b == d) or (a == b and c == d):
        return "Rectángulo"
    
    # Si no cumple ninguna de las anteriores
    else:
        return "Otro cuadrilátero"

# Pedimos al usuario que ingrese las medidas de los 4 lados
lados = []
for i in range(4):
    lado = float(input(f"Ingrese la medida del lado {i+1}: "))
    lados.append(lado)

# Identificamos el tipo de cuadrilátero
tipo_cuadrilatero = identificar_cuadrilatero(lados)
print(f"El cuadrilátero es: {tipo_cuadrilatero}")
