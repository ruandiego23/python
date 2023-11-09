class Person:
    eyes = 2

    def __init__(self, *children, name: str = None, age: int = None, country: str = None):
        self.children = ", ".join(list(children))
        self.name = name
        self.age = age
        self.country = country

    def greetings(self):
        greeting = f'Hello, my name is {self.name}.\n'
        return greeting

    @staticmethod
    def metodo_estatico():  # independe do objeto
        return 42

    @classmethod
    def atributes_names_of_class(cls):
        # Access class data
        atributes = f'{cls.eyes} eyes'
        return atributes


class Man(Person):

    def greetings_of_man(self):
        greeting_of_a_man = super().greetings()
        return f'{greeting_of_a_man}\tShake hand!'

    def __str__(self):
        return (
            f'\tName: {self.name}\n'
            f'\tAge: {self.age}\n'
            f'\tCountry: {self.country}\n'
            f'\tChildren: {self.children}\n'
        )


if __name__ == '__main__':
    diego = Man(name='Diego')
    juan = Man(name='Juan')
    olavo = Man(diego.name, juan.name, name='Olavo', age=74, country='Brazil')
    olavo.last_name = 'de Carvalho'  # dynamic attribute
    print(olavo.greetings_of_man())
    print()
    print(olavo)
    print(diego)
    print(id(olavo))
    print(olavo.name)
    print(olavo.age)
    del olavo.children
    olavo.eyes = 1
    del olavo.eyes  # apagando o atributo do objeto e não da classe
    print(olavo.name, olavo.last_name)
    print(olavo.__dict__)  # o tunder dict consegue acessar a lista de atributos do objeto
    print(diego.__dict__)
    print(Person.eyes)
    print(olavo.eyes)
    print(diego.eyes)
    print(id(diego.eyes), id(Person.eyes), id(olavo.eyes))
    print(Person.metodo_estatico(), olavo.metodo_estatico())
    print(Person.atributes_names_of_class(), olavo.atributes_names_of_class())
    pessoa = Person('Anônimo')
    print(isinstance(pessoa, Person))
    print(isinstance(pessoa, Man))  # a funçao isinstance serve para verificar se um objeto faz parte de uma classe
    print(isinstance(diego, Person))
    print(isinstance(olavo, Person))
    print(diego.eyes)
    print(diego.greetings_of_man())
    print(olavo.greetings_of_man())
