class Pessoa:
    olhos = 2  # atributo default(ou de classe)

    def __init__(self, *filhos, nome=None, idade=26):  # self é o objeto e idade e nome são os atributos(parametros)
        self.idade = idade  # o self.idade é nome desse objeto
        self.nome = nome  # o self.nome é o objeto
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá, meu nome é {self.nome}'

    @staticmethod
    def metodo_estatico():  # independe do objeto
        return 42

    @classmethod  # acessar dados da classe
    def nome_de_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos}'


class Homem(Pessoa):
    def cumprimentar(self):
        cumprimentar_da_classe = super().cumprimentar()  # o comando super serve para herdar os elementos da classe pai
        return f'{cumprimentar_da_classe}. Aperto de mão'


class Mutante(Pessoa):
    olhos = 3


if __name__ == '__main__':
    diego = Mutante(nome='Diego')  # diego é objeto(self) da função cumprimentar
    olavo = Homem(diego, nome='Olavo')  # olavo é o objeto o qual foi passado diego como filho
    print(Pessoa.cumprimentar(olavo))
    print(id(olavo))
    print(olavo.cumprimentar())
    print(olavo.nome)
    print(olavo.idade)
    for filho in olavo.filhos:
        print('filhos de Olavo:', filho.nome)
    olavo.sobrenome = 'de Carvalho'  # atributo dinâmico
    del olavo.filhos
    olavo.olhos = 1
    del olavo.olhos  # apagando o atributo do objeto e não da classe
    print(olavo.nome, olavo.sobrenome)
    print(olavo.__dict__)  # o tunder dict consegue acessar a lista de atributos do objeto
    print(diego.__dict__)
    print(Pessoa.olhos)
    print(olavo.olhos)
    print(diego.olhos)
    print(id(diego.olhos), id(Pessoa.olhos), id(olavo.olhos))
    print(Pessoa.metodo_estatico(), olavo.metodo_estatico())
    print(Pessoa.nome_de_atributos_de_classe(), olavo.nome_de_atributos_de_classe())
    pessoa = Pessoa('Anônimo')
    print(isinstance(pessoa, Pessoa))
    print(isinstance(pessoa, Homem))  # a funçao isinstance serve para verificar se um objeto faz parte de uma classe
    print(isinstance(diego, Pessoa))
    print(isinstance(olavo, Pessoa))
    print(diego.olhos)
    print(diego.cumprimentar())
    print(olavo.cumprimentar())
