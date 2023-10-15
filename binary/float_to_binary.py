import struct

number = 20.23

# pack the float as a binary string
s = struct.pack('!f', number)
print(s)

# convert each byte to binary and join them
b = ''.join(format(c, '08b') for c in s)
print(b)
