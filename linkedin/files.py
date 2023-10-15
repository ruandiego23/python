

def File():
    file = open('New.txt', 'w+')

    file.write("Linha gerada com a funcão 'File' \r\n")

    file.close()


def ChangeFile():
    file = open('New.txt', 'a+')

    file.write("Linha gerada com a funcão 'ChangeFile' \r\n")

    file.close()


ChangeFile()