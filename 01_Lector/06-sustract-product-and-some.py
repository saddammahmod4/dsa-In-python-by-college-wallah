"""
Q. Given a positive integer `num`, return the difference between
the product of its digits and the sum of its digits.

Formula:
    Answer = (Product of Digits) - (Sum of Digits)

Example 1:
Input: num = 234
Digits = 2, 3, 4
Product = 2 × 3 × 4 = 24
Sum = 2 + 3 + 4 = 9
Output: 15

Example 2:
Input: num = 121
Digits = 1, 2, 1
Product = 1 × 2 × 1 = 2
Sum = 1 + 2 + 1 = 4
Output: -2
"""

class Solution:
    def substractProductAndSum(self, num: int) -> int:
        temp = num
        num_sum = 0
        num_product = 1

        while temp > 0:
            reverse = temp % 10
            temp //= 10
            num_sum += reverse
            num_product *= reverse

        return num_product - num_sum


obj = Solution()

print(obj.substractProductAndSum(121))  # -2
print(obj.substractProductAndSum(234))  # 15

class Solution:
    def substractProductAndSum(self, num: int) -> int:
        temp = num
        num_sum = 0
        num_product = 1

        while temp > 0:
            reverse = temp % 10
            temp //= 10
            num_sum += reverse
            num_product *= reverse

        return num_product - num_sum

obj = Solution()
print(obj.substractProductAndSum(121))
print(obj.substractProductAndSum(234))

