def suma(a, b):
    return a + b

def resta(a, b):
    return a - b

def multiplicar(a, b):
    return a * b

def dividir(a, b):
    if b == 0:
        return "No se puede dividir por cero"
    return a / b

print("Calculadora simple en Python")
x = float(input("Primer número: "))
y = float(input("Segundo número: "))

print("Suma:", suma(x, y))
print("Resta:", resta(x, y))
print("Multiplicación:", multiplicar(x, y))
print("División:", dividir(x, y))