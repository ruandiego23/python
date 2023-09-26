
# word = 'house'.encode('utf-8')
# print(word)
# hex_word = word.hex()
# print(hex_word)


def get_hex(value):
    convert_string = int(value)
    convert_hex = hex(convert_string)
    return f'hexadecimal: {convert_hex},\nnumber: {convert_string}'


a = get_hex('564')
print(a)
