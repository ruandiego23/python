import timeit

print(timeit.timeit(stmt='["red", "blue", "green", 5, 7, 12, 18, "dude"]', number=10_000_000))

print(timeit.timeit(stmt='("red", "blue", "green", 5, 7, 12, 18, "dude")', number=10_000_000))
