"""
Parsing byte

Mask:
00000000
||||''''--> first value
|||'------> second value
|''-------> third value
'---------> fourfh value

Exercise:
* Separete the values with bitwise operators to get the exact decimal value
"""

# raw: 10111010 (186)
# va1: 00001010 (10)  >> 0
# va2: 00010000 (16)  >> 4
# va3: 00100000 (32)  >> 5
# va4: 10000000 (128) >> 7

data_32 = 186

value_1_mask = 15
value_2_mask = 16
value_3_mask = 96
value_4_mask = 128

value_1 = data_32 & value_1_mask
value_2 = (data_32 & value_2_mask) >> 4
value_3 = (data_32 & value_3_mask) >> 5
value_4 = (data_32 & value_4_mask) >> 7

print(value_1, value_2, value_3, value_4, sep=', ')
# 10, 1, 1, 1
