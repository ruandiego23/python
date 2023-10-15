"""
Python zip() with Dictionary

The zip() function in Python is used to combine two or more iterable dictionaries into a single iterable,
where corresponding elements from the input iterable are paired together as tuples. When using zip() with
dictionaries, it pairs the keys and values of the dictionaries based on their position in the dictionary."""

stocks = ['GEEKS', 'For', 'geeks']
prices = [2175, 1127, 2750]

new_dict = {stocks: prices for stocks, prices in zip(stocks, prices)}
print(new_dict, '\n')
"""
Python zip() with Multiple Iterables

Python’s zip() function can also be used to combine more than two iterables. It can take multiple iterables as input 
and return an iterable of tuples, where each tuple contains elements from the corresponding positions of the input 
iterables."""

list1 = [1, 2, 3]
list2 = ['a', 'b', 'c']
list3 = ['x', 'y', 'z']
zipped = [[list1, list2, list3] for list1, list2, list3 in zip(list1, list2, list3)]
print(zipped, '\n')

"""
Python zip() with Tuple

When used with tuples, zip() works by pairing the elements from tuples based on their positions. The resulting 
iterable contains tuples where the i-th tuple contains the i-th element from each input tuple."""

tuple1 = (1, 2, 3)
tuple2 = ('a', 'b', 'c')
zipped = zip(tuple1, tuple2)
result = list(zipped)
print(result)

"""
Unzipping Using zip()

Unzipping means converting the zipped values back to the individual self as they were. This is done with the help of “*”
operator.
"""

# Python code to demonstrate the working of
# unzip

# initializing lists
name = ["Manjeet", "Nikhil", "Shambhavi", "Astha"]
roll_no = [4, 1, 3, 2]
marks = [40, 50, 60, 70]

# using zip() to map values
mapped = zip(name, roll_no, marks)

# converting values to print as list
mapped = list(mapped)

# printing resultant values
print("The zipped result is : ", end="")
print(mapped)

print()

# unzipping values
namz, roll_noz, marksz = zip(*mapped)

print("The unzipped result: \n", end="")

# printing initial lists
print("The name list is : ", end="")
print(namz)

print("The roll_no list is : ", end="")
print(roll_noz)

print("The marks list is : ", end="")
print(marksz)

"""
Practical Applications

There are many possible applications that can be said to be executed using zip, be it student database or scorecard or
any other utility that requires mapping of groups. A small example of a scorecard is demonstrated below. 
"""

# Python code to demonstrate the application of
# zip()

# initializing list of players.
players = ["Sachin", "Sehwag", "Gambhir", "Dravid", "Raina"]

# initializing their scores
scores = [100, 15, 17, 28, 43]

# printing players and scores.
for pl, sc in zip(players, scores):
    print("Player : %s	 Score : %d" % (pl, sc))