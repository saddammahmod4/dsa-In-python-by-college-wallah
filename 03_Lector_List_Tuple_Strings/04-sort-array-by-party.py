"""
LeetCode 905. Sort Array By Parity

Question:
Given an integer array `nums`, move all the even integers to the beginning
of the array, followed by all the odd integers.

The relative order of even or odd numbers does not matter.

Return the modified array.

Example 1:
Input:
nums = [3, 1, 2, 4]

Output:
[2, 4, 3, 1]

Explanation:
Even numbers: 2, 4
Odd numbers : 3, 1

All even numbers appear before all odd numbers.

----------------------------------------------------

Example 2:
Input:
nums = [0]

Output:
[0]

Explanation:
There is only one element, which is even.
"""

from typing import List


class Solution:
    def sortArrayByParity(self, nums: List[int]) -> List[int]:

        # Total number of elements.
        n = len(nums)

        # 'start' points to the position where the next even
        # number should be placed.
        start = 0

        # Traverse the array.
        for i in range(n):

            # Check if the current number is even.
            if nums[i] % 2 == 0:

                # Swap the current even number with the element
                # at the 'start' position.
                temp = nums[i]
                nums[i] = nums[start]
                nums[start] = temp

                # Move the pointer to the next position.
                start += 1

        # Return the modified array.
        return nums


obj = Solution()

print(obj.sortArrayByParity([3, 1, 2, 4]))   # Output: [2, 4, 3, 1]