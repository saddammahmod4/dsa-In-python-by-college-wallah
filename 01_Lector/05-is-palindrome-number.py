"""
Question:
Given an integer `num`, determine whether it is a palindrome.

A palindrome number is a number that reads the same forward and backward.

Return:
- True if `num` is a palindrome.
- False otherwise.

Example 1:
Input:  num = 121
Output: True

Explanation:
Forward : 121
Backward: 121
Both are the same.

Example 2:
Input:  num = 71317
Output: True

Explanation:
Forward : 71317
Backward: 71317
Both are the same.

Example 3:
Input:  num = 12345
Output: False

Explanation:
Forward : 12345
Backward: 54321
They are different.
"""

class Solution:
    def isPalindromNumber(self, num: int) -> bool:
        temp = num
        reverse_number = 0

        while temp > 0:
            reminder = temp % 10
            reverse_number = (reverse_number * 10 + reminder)
            temp //= 10

        return num == reverse_number

obj = Solution()
print(obj.isPalindromNumber(121))
print(obj.isPalindromNumber(71317))
print(obj.isPalindromNumber(12345))