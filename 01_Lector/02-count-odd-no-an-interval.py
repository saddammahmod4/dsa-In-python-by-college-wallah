"""
Question:
Given two non-negative integers `low` and `high`, return the number of odd numbers
between `low` and `high` (inclusive).

Example 1:
Input:  low = 3, high = 7
Output: 3

Explanation:
Odd numbers between 3 and 7 are: 3, 5, 7
Count = 3

Example 2:
Input:  low = 5, high = 10
Output: 3

Explanation:
Odd numbers between 5 and 10 are: 5, 7, 9
Count = 3

Example 3:
Input:  low = 8, high = 10
Output: 1

Explanation:
Odd number between 8 and 10 is: 9
Count = 1
"""

class Solution:
    def countOddNoAnInterval(self, low: int, high: int) -> int:
        # Count odd numbers from 1 to high.
        odd_upto_high = (high + 1) // 2

        # Count odd numbers from 1 to (low - 1).
        # These are excluded from the required range.
        odd_before_low = (low - 1) // 2

        # Odd numbers in the range [low, high].
        return odd_upto_high - odd_before_low


obj = Solution()
print(obj.countOddNoAnInterval(5, 10))