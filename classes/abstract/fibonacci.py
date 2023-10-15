def check_index(key):
    """
    Is the given key an acceptable index?
    To be acceptable, the key should be a non-negative integer. If it
    is not an integer, a TypeError is raised; if it is negative, an
    IndexError is raised (since the sequence is of infinite length).
    """
    if not isinstance(key, int):
        raise TypeError
    if key < 0:
        raise IndexError


class Fibonacci:

    def __init__(self):
        self.a = 0
        self.b = 1
        self.values = [self.a, self.b]

    def __getitem__(self, item):
        """
        Get an item from the Fibonacci sequence.
        """
        check_index(key=item)

        return self.values[item]

    def __repr__(self):
        return f'{self.values}'

    def __next__(self):
        result = self.a
        self.a, self.b = self.b, self.a + self.b
        return result

    def __iter__(self):
        return self


if __name__ == '__main__':
    fib = Fibonacci()
    print("Fibonacci sequence below:")
    for _ in range(7):
        print(next(fib), end=" ")
