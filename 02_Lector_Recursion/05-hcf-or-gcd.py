"""
Question:
Given two positive integers `a` and `b`, find their Highest Common Factor (HCF),
also known as the Greatest Common Divisor (GCD).

The HCF/GCD is the largest positive integer that divides both numbers without
leaving a remainder.

Use recursion and the Euclidean Algorithm to solve the problem.

Example 1:
Input:  a = 15, b = 50
Output: 5

Explanation:
Factors of 15: 1, 3, 5, 15
Factors of 50: 1, 2, 5, 10, 25, 50
Greatest common factor = 5
"""

class Solution:

    def hcf(self, a, b):
        # Base case:
        # When the second number becomes 0,
        # the first number is the HCF.
        if b == 0:
            return a

        # Recursive case:
        # Replace (a, b) with (b, a % b)
        # until b becomes 0.
        return self.hcf(b, a % b)


obj = Solution()
print(obj.hcf(15, 50))   # Output: 5