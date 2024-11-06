"""Classe Bomba de Combustível: Faça um programa completo utilizando classes e métodos que:

a) Possua uma classe chamada bombaCombustível, com no mínimo esses atributos:
I.   tipoCombustivel.
II.  valorLitro
III. quantidadeCombustivel
b) Possua no mínimo esses métodos:
I.   abastecerPorValor( ) – método onde é informado o valor a ser abastecido e mostra a quantidade de litros que foi colocada no veículo
II.  abastecerPorLitro( ) – método onde é informado a quantidade em litros de combustível e mostra o valor a ser pago pelo cliente.
III. alterarValor( ) – altera o valor do litro do combustível.
IV.  alterarCombustivel( ) – altera o tipo do combustível.
V.   alterarQuantidadeCombustivel( ) – altera a quantidade de combustível restante na bomba.
OBS: Sempre que acontecer um abastecimento é necessário atualizar a quantidade de combustível total na bomba.

"""


class BombaCombustivel:
    def __init__(self, tipo_combustivel: str, valor_litro: float, quantidade_combustivel: float):
        self.quantidade_combustivel = quantidade_combustivel
        self.valor_litro = valor_litro
        self.tipo_combustivel = tipo_combustivel

    def abastecer_por_valor(self, valor: float):
        litros_abastecidos = valor / self.valor_litro
        self.__apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

    def __apresentar_abastecimento_se_possivel(self, litros_abastecidos: float, valor: float):
        if litros_abastecidos > self.quantidade_combustivel:
            print(f'Não é possível abastecer, faltam  {litros_abastecidos - self.quantidade_combustivel} litros')
            print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}.')
        else:
            self.quantidade_combustivel -= litros_abastecidos
            print(f'Foram abastecidos {litros_abastecidos:.2f} litros a valor de R$ {valor:.2f}')
            print(f'Sobraram na bomba {self.quantidade_combustivel:.2f} litros de {self.tipo_combustivel}.')

    def abastecer_por_litros(self, litros_abastecidos: float):
        valor = litros_abastecidos * self.valor_litro
        self.__apresentar_abastecimento_se_possivel(litros_abastecidos, valor)

    def adicionar_mais_combustivel(self, quantidade: float):
        if quantidade >= 0:
            self.quantidade_combustivel += quantidade
        else:
            print('Malandro, você não vai roubar combustível dessa bomba.')


bomba = BombaCombustivel('Gasolina', 6.5, 55.0)

bomba.abastecer_por_valor(100)
print()
bomba.abastecer_por_litros(150)
print()
bomba.adicionar_mais_combustivel(-50)
