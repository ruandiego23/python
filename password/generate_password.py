import string
import random

characters = string.ascii_letters + string.digits + string.punctuation
password = ''.join(random.choice(characters) for i in range(8))

print(f'Your password is: {password}')
