from typing import List


def fibonacci() -> List:
    num = int(input('How many Fibonacci numbers do you want? '))
    fibs = [0, 1]
    for _ in range(num - 2):
        fibs.append(fibs[-2] + fibs[-1])
    return fibs


if __name__ == '__main__':
    print(*fibonacci())
