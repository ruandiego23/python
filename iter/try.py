

def try_function():
    """ Create a function that returns a float or an int number
    :param
    :return -> str
    """
    while True:
        try:
            number: int = int(input('Type a number: '))
        except ValueError as ve:
            print("It isn't a number!\n", ve)
        else:
            if 0 <= number < 10:
                print(f"It is a Decimal Number: {number}")
                break
            else:
                print('The number has typed is invalid!\n'
                      'Try again.\n')


try_function()
