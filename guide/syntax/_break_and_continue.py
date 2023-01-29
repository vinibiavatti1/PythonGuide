###############################################################################
# Break and Continue
###############################################################################


# Break
# * The break keyword stops the iteration
for i in range(50):
    print(i, end=', ')
    if i == 5:
        break  # Jump out of loop
print()
# 0, 1, 2, 3, 4, 5,


# Continue
# * The continue keyword skips the rest of the loop code
for i in range(10):
    if i % 2 != 0:
        continue  # Skip and process the next element
    print(i, end=', ')
print()
# 0, 2, 4, 6, 8,





###############################################################################
# Break and continue
###############################################################################


# Break
# * Breaks the loop
i = 0
while i < 10:
    i += 1
    if i > 5:
        break
    print(i, end=', ')
print()
# 1, 2, 3, 4, 5,


# Continue
# * Skips the rest of the loop code
i = 0
while i < 10:
    i += 1
    if i % 2 != 0:
        continue
    print(i, end=', ')
print()
# 2, 4, 6, 8, 10,
