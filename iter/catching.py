"""
#154
Catching the Object
If you want access to the exception object itself in an except clause, you can use two arguments instead of
one. (Note that even when you are catching multiple exceptions, you are supplying except with only one
argument—a tuple.) This can be useful (for example) if you want your program to keep running but you
want to log the error somehow (perhaps just printing it out to the user). The following is a sample program
that prints out the exception (if it occurs) but keeps running:
"""

while True:
    try:
        x = int(input('Enter the first number: '))
        y = int(input('Enter the second number: '))
        z = x / y
        print(z)

    except Exception as e:  # or can be just expect
        print('Invalid input:', e)
        print('Please try again')
    else:
        break
