def pedir(num1, num2):
    num1 = int(input("Ingresa el primer numero:"))
    num1 = int(input("Ingresa el primer numero:"))


def sumar(num1,num2):
    suma = num1 + num2
    print("El resultado de la suma es: {}".format(suma))
    main()

def restar(num1,num2):
    resta = num1 - num2
    print("El resultado de la suma es: {}".format(resta))
    main()

def multiplicar(num1,num2):
    mult = num1 * num2
    print("El resultado de la suma es: {}".format(mult))
    main()

def dividir(num1,num2):
    resta = num1 / num2
    print("El resultado de la suma es: {}".format(resta))
    main()

def salir():
    print("Gracias por usar la")

def main():
    print("Elige la opción del menú: \n 1.-Sumar \n 2.-Restar \n 3.-Multiplicar \n 4.-Dividir \n 5.-Salir")

if __name__ == "__main__":
    main()



