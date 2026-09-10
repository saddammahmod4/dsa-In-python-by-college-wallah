"""
LeetCode 1480. Running Sum of 1d Array

Question:
Given an array of integers `nums`, return the running sum of the array.

The running sum at index `i` is the sum of all elements from index `0` to `i`.

Formula:
runningSum[i] = nums[0] + nums[1] + ... + nums[i]

Example 1:
Input:  nums = [1, 2, 3, 4]
Output: [1, 3, 6, 10]

Explanation:
Running Sum:
Index 0: 1
Index 1: 1 + 2 = 3
Index 2: 1 + 2 + 3 = 6
Index 3: 1 + 2 + 3 + 4 = 10

Example 2:
Input:  nums = [3, 1, 2, 10, 1]
Output: [3, 4, 6, 16, 17]

Explanation:
Running Sum:
Index 0: 3
Index 1: 3 + 1 = 4
Index 2: 3 + 1 + 2 = 6
Index 3: 3 + 1 + 2 + 10 = 16
Index 4: 3 + 1 + 2 + 10 + 1 = 17
"""

from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:

        # Get the total number of elements.
        n = len(nums)

        # Store the running sum.
        output = []

        # The first running sum is always the first element itself.
        output.append(nums[0])

        # Start from the second element.
        for i in range(1, n):

            # Current running sum =
            # Previous running sum + Current element.
            x = output[i - 1] + nums[i]

            # Add the running sum to the output list.
            output.append(x)

        # Return the final running sum array.
        return output


obj = Solution()
print(obj.runningSum([1, 2, 3, 4]))  # Output: [1, 3, 6, 10]