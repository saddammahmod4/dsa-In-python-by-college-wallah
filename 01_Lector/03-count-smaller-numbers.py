"""
LeetCode 1365. How Many Numbers Are Smaller Than the Current Number

Question:
Given an array of integers `nums`, return an array `result` where
`result[i]` is the number of elements in `nums` that are smaller than `nums[i]`.

Example 1:
Input:  nums = [8, 1, 2, 2, 3]
Output: [4, 0, 1, 1, 3]

Explanation:
8 -> Four numbers are smaller: 1, 2, 2, 3
1 -> No numbers are smaller.
2 -> One number is smaller: 1
2 -> One number is smaller: 1
3 -> Three numbers are smaller: 1, 2, 2

Example 2:
Input:  nums = [6, 5, 4, 8]
Output: [2, 1, 0, 3]

Explanation:
6 -> Smaller numbers: 5, 4 (Count = 2)
5 -> Smaller number: 4 (Count = 1)
4 -> No smaller numbers (Count = 0)
8 -> Smaller numbers: 6, 5, 4 (Count = 3)
"""

from typing import List

class Solution:
    def smallNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        output = []
        for i in nums:
            count = 0
            for j in nums:
                if i > j:
                    count += 1
            output.append(count)
            count = 0
        return output

obj = Solution()
print(obj.smallNumbersThanCurrent([8, 1, 2, 2, 3]))