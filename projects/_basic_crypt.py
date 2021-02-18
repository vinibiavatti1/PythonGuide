"""
Basic Crypt Algorithm

* Encrypt: The algorithm gets the string, convert to ascii codes and add the
  key value for each code
* Decrypt: The algorithm gets the string, convert to ascii codes and subtract
  the key value for each code
* NOTE: Execute it in TERMINAL
"""


def encrypt(txt, key):
    return ''.join([chr(ord(c) + key) for c in txt])


def decrypt(txt, key):
    return ''.join([chr(ord(c) - key) for c in txt])


# Text
text = input('Type a string to encrypt/decrypt:')


# Key
key = input('Type a key (int):')
if not key.isdigit():
    print('Invalid key')
    exit()
key = int(key)


# Operation
operation = input('Choose a operation: Encrypt (e) / Decrypt (d):')
if operation == 'e':
    print(encrypt(text, key))
elif operation == 'd':
    print(decrypt(text, key))
else:
    print('Invalid operation')
