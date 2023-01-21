def sumar(num1,num2):
    suma = num1 + num2
    print("El resultado de la suma es: {}".format(suma))

def restar(num1,num2):
    resta = num1 - num2
    print("El resultado de la suma es: {}".format(resta))

def multiplicar(num1,num2):
    mult = num1 * num2
    print("El resultado de la suma es: {}".format(mult))

def dividir(num1,num2):
    resta = num1 / num2
    print("El resultado de la suma es: {}".format(resta))


def main():
    print("Elige la opción del menú: \n 1.-Sumar \n 2.-Restar \n 3.-Multiplicar \n 4.-Dividir \n 5.-Salir")

if __name__ == "__main__":
    main()

opcion = int(input("Ingrese una opcion: "))

num1 = int(input("Ingresa el primer numero:"))
num2 = int(input("Ingresa el primer numero:"))

while opcion < 5:
    if opcion == 1:
      sumar(num1,num2)
    elif opcion == 2:
      restar(num1,num2)
    elif opcion == 3:
      multiplicar(num1,num2)
    elif opcion == 4:
      dividir(num1,num2)