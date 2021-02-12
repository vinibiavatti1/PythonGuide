"""
While examples
"""
# While
i = 0
while i < 10:
    i += 1
    print(i, end=', ') # 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 
print()

# Break
i = 0
while i < 10:
    i += 1
    if i > 5:
        break
    print(i, end=', ') # 1, 2, 3, 4, 5, 
print()

# Continue
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=', ') # 2, 4, 6, 8, 10, 
print()

# Else
i = 0
while i < 5:
    i += 1
    print(i, end=', ') # 1, 2, 3, 4, 5, end
else:
    print('end')

# While true
while True:
    break
