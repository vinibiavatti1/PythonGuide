"""
Bitwise 8bit sum

* Used concepts of half adder and full adder
"""


class ALU8bitSum():

    b1_mask = 2 ** 0
    b2_mask = 2 ** 1
    b3_mask = 2 ** 2
    b4_mask = 2 ** 3
    b5_mask = 2 ** 4
    b6_mask = 2 ** 5
    b7_mask = 2 ** 6
    b8_mask = 2 ** 7

    def sum(self, x, y):
        """
        Sum x and y using bitwise operators
        """
        b1_x = (x & ALU8bitSum.b1_mask)
        b2_x = (x & ALU8bitSum.b2_mask) >> 1
        b3_x = (x & ALU8bitSum.b3_mask) >> 2
        b4_x = (x & ALU8bitSum.b4_mask) >> 3
        b5_x = (x & ALU8bitSum.b5_mask) >> 4
        b6_x = (x & ALU8bitSum.b6_mask) >> 5
        b7_x = (x & ALU8bitSum.b7_mask) >> 6
        b8_x = (x & ALU8bitSum.b8_mask) >> 7

        b1_y = (y & ALU8bitSum.b1_mask)
        b2_y = (y & ALU8bitSum.b2_mask) >> 1
        b3_y = (y & ALU8bitSum.b3_mask) >> 2
        b4_y = (y & ALU8bitSum.b4_mask) >> 3
        b5_y = (y & ALU8bitSum.b5_mask) >> 4
        b6_y = (y & ALU8bitSum.b6_mask) >> 5
        b7_y = (y & ALU8bitSum.b7_mask) >> 6
        b8_y = (y & ALU8bitSum.b8_mask) >> 7

        r1, carry = self.half_adder(b1_x, b1_y)
        r2, carry = self.full_adder(b2_x, b2_y, carry)
        r3, carry = self.full_adder(b3_x, b3_y, carry)
        r4, carry = self.full_adder(b4_x, b4_y, carry)
        r5, carry = self.full_adder(b5_x, b5_y, carry)
        r6, carry = self.full_adder(b6_x, b6_y, carry)
        r7, carry = self.full_adder(b7_x, b7_y, carry)
        r8, carry = self.full_adder(b8_x, b8_y, carry)

        return self.parse_result(r1, r2, r3, r4, r5, r6, r7, r8)

    def parse_result(self, r1, r2, r3, r4, r5, r6, r7, r8):
        """
        Parse bit data to decimal value
        """
        result = (r1) | \
            (r2 << 1) | \
            (r3 << 2) | \
            (r4 << 3) | \
            (r5 << 4) | \
            (r6 << 5) | \
            (r7 << 6) | \
            (r8 << 7)
        return result

    def half_adder(self, b1, b2):
        """
        Half adder truth table processor
        x y   r c
        0 0 > 0 0
        0 1 > 1 0
        1 0 > 1 0
        1 1 > 0 1
        """
        result = b1 ^ b2
        carry = b1 & b2
        return result, carry

    def full_adder(self, b1, b2, carry):
        """
        Full adder truth table processor
        x y c   r c
        0 0 0 > 0 0
        0 0 1 > 1 0
        0 1 0 > 1 0
        0 1 1 > 0 1
        1 0 0 > 1 0
        1 0 1 > 0 1
        1 1 0 > 0 1
        1 1 1 > 1 1
        """
        result = (b1 ^ b2) ^ carry
        carry = ((b1 ^ b2) & carry) | (b1 & b2)
        return result, carry


# Entry
x = 10  # 00001010
y = 6   # 00000110
alu = ALU8bitSum()
result = alu.sum(x, y)
print(result)
# 16
