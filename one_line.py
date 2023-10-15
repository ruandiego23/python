import datetime; print("Days left to new year:", (datetime.date(2023, 12, 31) - datetime.date.today()).days, "days")

squares = (i*i for i in range(10) if i % 2 == 0 or i % 3 == 0)
print("Squares in range(10) if i % 2 == 0 or i % 3 == 0:\n", *squares)

var = 42 if 3 > 2 else 50
print(var)
days = 0


names = [line.rstrip() for line in open("names.txt", "r")]
print(*names)


age = 28
valid = "You're an adult"
invalid = "You're NOT an adult"

print(valid) if age >= 18 else print(invalid)

countries = ['united States', 'brazil', 'china']

capitalized = [word.title() for word in countries]; print(capitalized)

# Join Dictionaries

dictionary = {'a': 1, 'b': 2}
dictionary2 = {'c': 3, 'd': 4}

merged = {**dictionary, **dictionary2}; print(merged)

mylist = [1, 2, 3, 4, 5]
print(list(filter(lambda x: x % 2 == 0, mylist)))

population = {"USA": 329.5, "Brazil": 203, "UK": 67.2}

mydict = {k: v for k, v in sorted(population.items(), key=lambda x: x[1])}
print(mydict)
