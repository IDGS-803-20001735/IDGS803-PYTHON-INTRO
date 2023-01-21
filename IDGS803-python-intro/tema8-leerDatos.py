print("Pedir dos numeros")

#  int numeros sin punto decimal
#  float: numeros con punto decimal
#  str: para cadenas

num1 = int(input("Dame el primer número: "))
num2 = int(input("Dame el segundo número: "))

print("La suma de {} + {} = {}".format(num1, num2, (num1 + num2)))

dato1 = 100
dato2 = "23.7"

print(len(str(dato1)), "caraceres")
print(float(dato2))