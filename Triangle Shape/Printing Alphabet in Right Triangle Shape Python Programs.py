"""
        A
        B C
        C D E
        D E F G
        E F G H I
"""

n = int(input('Número de linhas: '))

for linha in range(n):
    k = ord("A") + linha
    for coluna in range(linha + 1):
        print(chr(k), end=' ')
        k = k + 1
    print()

print()
print('Teste da função ord e chr')

k = ord('a')
print('O número do símbolo "a" é ' + str(k))

print('O caracter que representa o numero 65 é ' + chr(65))
