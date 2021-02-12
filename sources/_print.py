"""
Print examples

The print() function prints the given object to the standard 
output device (screen) or to the text stream file.
Formats: print(*objects, sep=' ', end='\n', file=sys.stdout, flush=False)
"""
print('Hello World')            # Hello World
print('A', 'B', 'C', sep=' ')   # A B C
print(1, '2', sep=',')          # 1,2
print('Same ', end="")          
print('line!')                  # Same line!