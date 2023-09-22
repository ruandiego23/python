"""
This works and is a straightforward implementation. Basically, what it does is this: first, it sets the result to n;
then, the result is multiplied by each number from 1 to n–1 in turn; finally, it returns the result. But you can
do this differently if you like. The key is the mathematical definition of the factorial, which can be stated as
follows:
•The factorial of 1 is 1.
•The factorial of a number n greater than 1 is the product of n and the factorial of n–1.
As you can see, this definition is exactly equivalent to the one given at the beginning of this section.
Now consider how you implement this definition as a function. It is actually pretty straightforward, once
you understand the definition itself.
"""


def factorial(f):
    if f == 1:
        return 1
    else:
        return f * factorial(f - 1)


factorial(5)
