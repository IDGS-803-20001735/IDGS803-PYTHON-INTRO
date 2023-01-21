numero = int(input("Ingresa un número para generar la tabla de multiplicar: "))

def funcion(numero):
    for i in range(1,11):
        print("{} x {} = {}".format(numero, i,numero * i))

funcion(numero)