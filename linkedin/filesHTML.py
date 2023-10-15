from html.parser import HTMLParser


class MyParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        print("Tag de abertura encontrada!")
        if attrs.__len__() > 0:
            for a in attrs:
                print("  Valores encontrados  ", a[0], " = ", a[1])

    def handle_endtag(self, tag):
        print("Tag de fechamento encontrada")

    def handle_comment(self, data):
        print("Comentário encontrado.")

    def handle_data(self, data: str) -> None:
        print("Valores encontrados")
        if data.isspace():
            print("O valor encontrado é um espaço")
        else:
            print("O valor encontrado é: ", data)


def myObject():
    meuparser1 = MyParser()
    arquivo = open()
    dados = arquivo.read()  # coloque um path de um html
    meuparser1.feed(dados)