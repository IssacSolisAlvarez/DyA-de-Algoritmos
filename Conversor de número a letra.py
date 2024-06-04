from num2words import num2words

def numero_a_letras(numero):
    if numero < 1 or numero > 10**18:
        return "Número fuera de rango (1 - 1,000,000,000,000,000,000)"
    return num2words(numero, lang='es')

numero = int(input("Ingrese un número (1 - 1,000,000,000,000,000,000): "))

letras = numero_a_letras(numero)
print(f"El número {numero} en letras es: {letras}")
