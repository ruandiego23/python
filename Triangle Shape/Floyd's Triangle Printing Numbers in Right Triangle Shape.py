
n = int(input('Digite o número de linhas do triângulo: '))
num = 1

for linhas in range(1, n + 1):
    for colunas in range(1, linhas + 1):
        print(num, end=' ')
        num += 1
    print()
