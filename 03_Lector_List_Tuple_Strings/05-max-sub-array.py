"""
LeetCode 53. Maximum Subarray

Question:
Given an integer array `nums`, find the contiguous subarray
(a subarray containing at least one number) that has the largest sum.

Return the maximum possible sum.

Important:
- The elements must be contiguous.
- We need the maximum SUM, not the maximum element.

Example 1:
Input:
nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]

Output:
6

Explanation:
The subarray [4, -1, 2, 1] has the maximum sum.

4 + (-1) + 2 + 1 = 6

----------------------------------------------------

Example 2:
Input:
nums = [5, -1, -7, 6, 2, -3, 5, -10, 2]

Output:
10

Explanation:
The maximum subarray is:

[6, 2, -3, 5]

6 + 2 + (-3) + 5 = 10

----------------------------------------------------

Example 3:
Input:
nums = [-5, -2, -8]

Output:
-2

Explanation:
All numbers are negative, so we choose the largest
(single) number: -2.
"""

from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

        # Stores the sum of the current subarray.
        current_sum = 0

        # Start with the first element as the maximum sum.
        # This also handles arrays containing only negative numbers.
        max_sum = nums[0]

        # Go through every element in the array.
        for i in range(len(nums)):

            # Add the current number to the current subarray sum.
            current_sum += nums[i]

            # If the current subarray has a larger sum,
            # update the maximum sum.
            if current_sum > max_sum:
                max_sum = current_sum

            # If the current sum becomes negative,
            # discard the current subarray and start fresh.
            if current_sum < 0:
                current_sum = 0

        # Return the largest subarray sum found.
        return max_sum


obj = Solution()

print(obj.maxSubArray([5, -1, -7, 6, 2, -3, 5, -10, 2]))
# Output: 10