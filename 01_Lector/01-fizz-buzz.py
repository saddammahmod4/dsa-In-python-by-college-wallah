"""
LeetCode 412. Fizz Buzz

Question:
Given an integer n, return a list of strings from 1 to n where:
- If the number is divisible by 3, return "Fizz".
- If the number is divisible by 5, return "Buzz".
- If the number is divisible by both 3 and 5, return "FizzBuzz".
- Otherwise, return the number as a string.

Example:
Input:  n = 15

Output:
[
    "1", "2", "Fizz", "4", "Buzz",
    "Fizz", "7", "8", "Fizz", "Buzz",
    "11", "Fizz", "13", "14", "FizzBuzz"
]

Explanation:
1  -> "1"
2  -> "2"
3  -> "Fizz"      (divisible by 3)
4  -> "4"
5  -> "Buzz"      (divisible by 5)
6  -> "Fizz"
...
15 -> "FizzBuzz"  (divisible by both 3 and 5)
"""

from typing import List

class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        output = []

        for i in range(1, n+1):
            if (i % 3 == 0 and i % 5 == 0):
                output.append("FizzBuzz")
            elif i % 3 == 0:
                output.append("Fizz")
            elif i % 5 == 0:
                output.append("Buzz")
            else:
                output.append(str(i))

        return output

obj = Solution()
print(obj.fizzBuzz(20))
