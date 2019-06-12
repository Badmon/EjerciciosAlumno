
def Sumar(x,y):
    return x + y

def Restar(x,y):
    return x - y

def Multiplicar(x,y):
    return x * y

def Dividir(x,y):
    return x/y

def Potencia(x,y):
    return pow(x,y)

print("Seleccionar operación.")
print("1.Sumar")
print("2.Restar")
print("3.Multiplicar")
print("4.Dividir")
print("5.Potencia")
a=input("Ingrese la opcion:")
num1=int(input("num: "))
num2=int(input("num: "))

if a =='1':
    print(num1, "+", num2,"=", Sumar(num1,num2))

elif a == '2':
    print(num1, "-", num2,"=",Restar(num1,num2))

elif a == '3':
    print(num1, "x", num2,"=",Multiplicar(num1,num2))

elif a == '4':
    print(num1, "/", num2,"=",Dividir(num1,num2))

elif a == '5':
    print(num1, "^", num2,"=",Potencia(num1,num2))

else:
    print("Entrada invalidad")