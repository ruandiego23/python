class Person:
    eyes = 2

    def __init__(self, *children, name: str = None, age: int = None, country: str = None):
        self.children = list(children)
        self.name = name
        self.age = age
        self.country = country

    def greetings(self):
        greeting = f'Hello, my name is {self.name}'
        return greeting

    @classmethod
    def atributes_names_of_class(cls):
        # Access class data
        atributes = f'{cls.eyes} eyes'
        return atributes


class Man(Person):

    def greetings_of_man(self):
        #
        greeting_of_a_man = super().greetings()
        return f'{greeting_of_a_man}.\nShake hand!'

    def __str__(self):
        return (
            f'\tName: {self.name}\n'
            f'\tAge: {self.age}\n'
            f'\tCountry: {self.country}\n'
        )


if __name__ == '__main__':
    diego = Man(name='Diego')
    juan = Man(name='Juan')
    olavo = Man(diego, juan, age=74, country='Brazil', name='Olavo')

    print(olavo.greetings_of_man())
    print(str(olavo))


    def children_name():
        kids = [child.name for child in olavo.children]
        print(*kids)
    children_name()
