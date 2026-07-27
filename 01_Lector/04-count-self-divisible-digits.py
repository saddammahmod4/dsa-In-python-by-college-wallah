"""
Question:
You are given a positive integer `num`.

Return the number of digits in `num` that divide `num` evenly.

A digit divides `num` evenly if:
1. The digit is not 0.
2. `num % digit == 0`.

Example 1:
Input:  num = 1248
Output: 4

Explanation:
Digits are: 1, 2, 4, 8
1248 % 1 = 0 ✔
1248 % 2 = 0 ✔
1248 % 4 = 0 ✔
1248 % 8 = 0 ✔
Answer = 4

Example 2:
Input:  num = 121
Output: 2

Explanation:
Digits are: 1, 2, 1
121 % 1 = 0 ✔
121 % 2 = 1 ✘
121 % 1 = 0 ✔
Answer = 2

Example 3:
Input:  num = 7
Output: 1

Explanation:
Digit is: 7
7 % 7 = 0 ✔
Answer = 1
"""

class Solution:
    def countSelfDivisibleDigits(self, num: int) -> int:
        temp = num
        count = 0
        while temp > 0:

            # Extract the last digit.
            # Example: 1248 % 10 = 8
            reminder = temp % 10
            if num % reminder == 0:
                count += 1

            # Remove the last digit.
            # Example:
            # 1248 // 10 = 124
            # 124  // 10 = 12
            # 12   // 10 = 1
            # 1    // 10 = 0
            temp //= 10
        return count

obj = Solution()
print(obj.countSelfDivisibleDigits(1248))
print(obj.countSelfDivisibleDigits(121))
print(obj.countSelfDivisibleDigits(7))