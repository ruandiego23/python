palavra = 'DevPro'.upper()

print('Jogo da Forca')
print('Descubra a palavra')

print('A palavra é: ', end='')
for letra in palavra:
    print('_ ', end='')

conjunto_letras_palavras = set(palavra)
conjunto_letras_digitadas = set()

print(conjunto_letras_palavras)
print('O' in conjunto_letras_palavras)
print(conjunto_letras_palavras.issubset(conjunto_letras_digitadas))
print(conjunto_letras_digitadas.issubset(conjunto_letras_palavras))
erros = 0

while not conjunto_letras_palavras.issubset(conjunto_letras_digitadas) and erros < 7:
    print()
    print()
    letra_digitada = input('Digite uma letra: ').upper()
    conjunto_letras_digitadas.add(letra_digitada)
    if letra_digitada in conjunto_letras_palavras:
        for letra in palavra:
            if letra in conjunto_letras_digitadas:
                print(f'{letra} ', end='')
            else:
                print('_ ', end='')
    else:
        erros += 1
        print(f' -> Erro {erros} de 6. Tente de novo!')
    print()
    print('Letras já digitadas ', conjunto_letras_digitadas)

if erros < 7:
    print('Parabéns, você ganhou!')
else:
    print('Infelizmente você perdeu!')

    print('Letras já digitadas: ', conjunto_letras_digitadas)
