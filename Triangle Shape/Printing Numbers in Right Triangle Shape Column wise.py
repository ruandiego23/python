"""
        Ex:
        1
        2 6
        3 7 10
        4 8 11 13
        5 9 12 14 15
"""

num = int(input('Digite o número de linhas: '))

for linhas in range(num):
    val = linhas + 1
    dec = num - 1
    for colunas in range(linhas + 1):
        print(val, end=' ')
        val = val + dec
        dec = dec - 1
    print()
