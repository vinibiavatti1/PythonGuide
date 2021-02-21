"""
Binary representation
"""


def int_to_bin(number, size):
    binary = ''
    while number > 0:
        number, mod = divmod(number, 2)
        if mod == 1:
            binary += '1'
        else:
            binary += '0'
    return ''.join(list(reversed(binary))).zfill(size)


for num in range(256):
    print(int_to_bin(num, 8), ': ', num)
