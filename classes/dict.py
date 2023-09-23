
matrix = [[0, 1, 2], [3, 4, 5], [6, 7, 8]]

values = (value ** 2 for row in matrix for value in row)
print(*values)

values_enumerate = (row[0] for _, row in enumerate(matrix))
print(*values_enumerate)


# Dictionary Comprehensions
days = "Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday",

dict_days = {i: days[i - 1] for i in range(1, len(days) + 1)}
print(dict_days)
