def multiplicar_base(num1):
    def multiplicar(num2):
        return num1 * num2
    return multiplicar

duplicar = multiplicar_base(2)
triplicar = multiplicar_base(3)
quadriplicar = multiplicar_base(4)

print(duplicar(5))
print(triplicar(5))
print(quadriplicar(5))