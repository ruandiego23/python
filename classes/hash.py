
class Company:
    def __init__(self, name: str, id: int):
        self.name = name
        self.id = id

    def __str__(self):
        return self.name

    def __eq__(self, other):
        return self.name == other.name and self.id == other.id

    def __hash__(self):
        return hash((self.name, self.id))


emp1 = Company('Microsoft', 1)
emp2 = Company('Red Hard', 2)
emp3 = Company('Microsoft', 1)

print(emp1 == emp2)
print(emp1 == emp3)
