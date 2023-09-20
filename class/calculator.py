"""
Multiple Superclasses
I’m sure you noticed a small detail in the previous section that may have seemed odd: the plural form in
bases. I said you could use it to find the base classes of a class, which implies that it may have more than
one. This is, in fact, the case. To show how it works, let’s create a few classes.
"""


class Calculator:

    def __init__(self):
        self.value = None

    def calculate(self, expression):
        self.value = eval(expression)


class Talker(Calculator):

    def talk(self):
        print(f"Hy, my value is {self.value}")


class TalkingCalculator(Talker):
    pass


obj = TalkingCalculator()
obj.calculate('2 + 7')
obj.talk()
