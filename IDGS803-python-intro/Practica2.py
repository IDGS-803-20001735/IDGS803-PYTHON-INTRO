def sumar(num1,num2):
    print("{} + {} = {}".format(num1, num2, num1 + num2))

def restar(num1,num2):
    print("{} - {} = {}".format(num1, num2, num1 - num2))

def multiplicar(num1,num2):
    print("{} x {} = {}".format(num1, num2, num1 * num2))

def dividir(num1,num2):
    print("{} / {} = {}".format(num1, num2, num1 / num2))


def main():
    print("----BIENVENIDO A EL MENÚ---- \n 1.-Sumar \n 2.-Restar \n 3.-Multiplicar \n 4.-Dividir \n 5.-Salir")

if __name__ == "__main__":
    main()

opcion = int(input("Ingrese una opcion: "))

num1 = int(input("Ingresa el primer numero:"))
num2 = int(input("Ingresa el primer numero:"))

while opcion != 5:
    if opcion == 1:
      sumar(num1,num2)
    elif opcion == 2:
      restar(num1,num2)
    elif opcion == 3:
      multiplicar(num1,num2)
    elif opcion == 4:
      dividir(num1,num2)
    else:
       print("--- La opción elegida no se encuetra dentro del menú ---")

    main()
    opcion = int(input("Ingrese una opcion: "))

print("!!!Gracias por utilizar mi sistema!!!")



