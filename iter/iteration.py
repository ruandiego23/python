
def iteration():
    expr = [1, 2, 3]
    it = iter(expr)
    while True:
        try:
            x = next(it)
        except StopIteration:
            break
        else:
            print(x)


iteration()
