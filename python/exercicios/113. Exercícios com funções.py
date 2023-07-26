def multiplicar(*args) -> int | float:
    total = 1
    for i in args:
        total *= i
    return total

def par_impar(number) -> bool:
    return number % 2 == 0

resultado = multiplicar(1,3,9,5,2)
print(resultado)
print(par_impar(resultado))