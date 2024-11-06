"""
        Ex:
        1
        2 9
        3 8 10
        4 7 11 14
        5 6 12 13 15
"""

n = int(input('Digite o número de linhas: '))

for linhas in range(n):
    for colunas in range(linhas+1):
        x = 0
        for k in range(colunas):
            x = x + n - k
        if colunas % 2 == 0:
            print(x+linhas-colunas+1, end=' ')
        else:
            print(x+n-linhas, end=' ')
    print()
