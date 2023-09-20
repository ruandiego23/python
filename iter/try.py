from math import inf


def try_function():
    """ Create a function that returns a float or an int number
    :param
    :return -> str
    """
    while True:
        try:
            number: float = float(input('Type a number: '))
        except ValueError:
            print("It isn't a number")
        else:
            if -inf < number > 0:
                print(f"It is a Number: {number}")
                break
            else:
                print('The number has typed is invalid!\n'
                      'Try again.\n')


try_function()
