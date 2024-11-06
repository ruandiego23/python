"""
Faça um programa para imprimir:
    1
    2   2
    3   3   3
    .....
    n   n   n   n   n   n  ... n
para um n informado pelo usuário. Use uma função que receba um valor n inteiro e imprima até a n-ésima linha.
"""


def triangle(n: int):
    for i in range(n):
        i = i + 1
        for _ in range(i):
            print(i, end=' ')
        print()


print('Triangulo 1')
triangle(5)


def triangle_2(n: int):
    for i in range(n):
        i = i + 1
        for j in range(i):
            print(j + 1, end=' ')
        print()


print('Triângulo 2')
triangle_2(5)


def triangle_3(n: int):
    for i in range(n):
        for j in range(i, -1, -1):
            print(j + 1, end=' ')
        print()


print('Triângulo 3')
triangle_3(5)


def triangle_4(n: int):
    for i in range(n):
        for j in range(i + 1):
            print(n - i, end=' ')
        print()


print('Triângulo 5')
triangle_4(5)


def triangle_5(n: int):
    for i in range(n):
        for j in range(i + 1):
            print(n - j, end=' ')
        print()


print('Triângulo 5')
triangle_5(5)


def triangle_6(n: int):
    for i in range(n):
        for j in range(i, -1, -1):
            print(n - j, end=' ')
        print()


print('Triângulo 6')
triangle_6(5)
