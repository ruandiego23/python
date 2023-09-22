
def factorial(n):
    if n == 1:
        return n
    else:
        result = n * factorial(n - 1)
        return result


def power(x, n):
    if n == 0:
        return 1
    else:
        result = x * power(x, n - 1)
        return result


if __name__ == "__main__":
    print(factorial(5))
    print(power(5, 3))
