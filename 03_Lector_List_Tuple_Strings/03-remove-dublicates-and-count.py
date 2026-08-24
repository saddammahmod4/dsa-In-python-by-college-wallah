"""
LeetCode 26. Remove Duplicates from Sorted Array

Question:
Given a sorted integer array `nums`, remove the duplicates in-place so that
each unique element appears only once.

Return the number of unique elements.

The first `k` elements of `nums` should contain the unique values, where `k`
is the returned count.

Note:
- Do not create another array.
- Modify the original array in-place.
- The input array is sorted, so duplicate elements are adjacent.

Example 1:
Input:
nums = [1, 1, 2]

Output:
2

Modified nums:
[1, 2, ...]

Explanation:
There are 2 unique numbers: 1 and 2.

----------------------------------------------------

Example 2:
Input:
nums = [1, 2, 2, 3, 3, 4, 4, 5]

Output:
5

Modified nums:
[1, 2, 3, 4, 5, 4, 4, 5]

Explanation:
Unique elements are:
1, 2, 3, 4, 5

The function returns 5.
Only the first 5 positions are important.
The remaining values can be anything.
"""

from typing import List


class Solution:
    def removeDuplicatesAndCount(self, nums: List[int]) -> int:

        # Total number of elements.
        n = len(nums)

        # 'start' points to the last unique element found.
        # Initially, the first element is always unique.
        start = 0

        # Traverse the array from the second element.
        for i in range(1, n):

            # If the current element is different from the last unique element,
            # we've found a new unique value.
            if nums[start] != nums[i]:

                # Move the unique pointer forward.
                start += 1

                # Place the new unique element at the next position.
                nums[start] = nums[i]

        # Number of unique elements = last index + 1
        return start + 1


obj = Solution()

nums = [1, 2, 2, 3, 3, 4, 4, 5]
count = obj.removeDuplicatesAndCount(nums)

print("Unique Count:", count)