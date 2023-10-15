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

    print(olavo.greetings_of_man())
    print()
    print(olavo)
    print(diego)
