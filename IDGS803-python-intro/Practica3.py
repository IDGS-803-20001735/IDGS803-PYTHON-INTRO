class operationsBasic():

    def sumar(self, num1,num2):
        print("{} + {} = {}".format(num1, num2, num1 + num2))

    def restar(self, num1,num2):
        print("{} - {} = {}".format(num1, num2, num1 - num2))

    def multiplicar(self, num1,num2):
        print("{} x {} = {}".format(num1, num2, num1 * num2))

    def dividir(self, num1,num2):
        print("{} / {} = {}".format(num1, num2, num1 / num2))


def main():
      print("----BIENVENIDO A EL MENÚ---- \n 1.-Sumar \n 2.-Restar \n 3.-Multiplicar \n 4.-Dividir \n 5.-Salir")

      opcion = int(input("Ingrese una opción: "))

      obj = operationsBasic()

      while opcion != 5:
            
            num1 = int(input("Ingresa el primer número:"))
            num2 = int(input("Ingresa el primer número:")) 

            if opcion == 1:
              obj.sumar(num1,num2)
            elif opcion == 2:
              obj.restar(num1,num2)
            elif opcion == 3:
              obj.multiplicar(num1,num2)
            elif opcion == 4:
              obj.dividir(num1,num2)
            else:
              print("--- La opción elegida no se encuetra dentro del menú ---")

            opcion = int(input("Ingrese una opcion: "))
            
if __name__ == "__main__":
   main()
