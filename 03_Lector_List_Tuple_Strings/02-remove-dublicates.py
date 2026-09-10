"""
Question:
Given a sorted integer array `nums`, remove the duplicate elements and
return a list containing only the unique elements.

Since the array is already sorted, duplicate values always appear next to
each other.

Example 1:
Input:  nums = [1, 1, 2]
Output: [1, 2]

Explanation:
- Keep the first 1.
- Skip the second 1 because it is a duplicate.
- Keep 2.
Result = [1, 2]

Example 2:
Input:  nums = [1, 1, 2, 2, 3, 4]
Output: [1, 2, 3, 4]

Explanation:
Original Array:
[1, 1, 2, 2, 3, 4]

Unique Elements:
[1, 2, 3, 4]
"""

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> List[int]:

        # Store unique elements.
        output = []

        # The first element is always unique.
        output.append(nums[0])

        # Start checking from the second element.
        for i in range(1, len(nums)):

            # Compare the current number with the last unique number.
            # If they are different, it is a new unique value.
            if output[-1] != nums[i]:
                output.append(nums[i])

        # Return the list of unique elements.
        return output


obj = Solution()
print(obj.removeDuplicates([1, 1, 2, 2, 3, 4]))  # Output: [1, 2, 3, 4]