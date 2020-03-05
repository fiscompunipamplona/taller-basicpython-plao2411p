#Ejercicio: escriba un código que calcule la secuencia de Fibonacci hasta 1000

def fib(n):
    a=0
    b=1
    while a < n:
        print(a, end=' ')
        a, b = b, a+b
    print()
fib(1000)

