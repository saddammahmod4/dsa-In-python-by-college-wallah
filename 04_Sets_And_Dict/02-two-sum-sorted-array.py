"""
Question:
Given a sorted array of integers `nums` and an integer `target`,
find two different numbers whose sum is equal to the target.

Return the indexes of those two numbers.

Rules:
- The array is sorted in ascending order.
- You cannot use the same element twice.
- Return an empty list if no valid pair is found.

Example 1:
Input:
nums = [2, 3, 8, 11, 20, 35, 52]
target = 23

Output:
[1, 4]

Explanation:
nums[1] = 3
nums[4] = 20

3 + 20 = 23

Therefore, return [1, 4].

----------------------------------------------------

Example 2:
Input:
nums = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Explanation:
nums[0] = 2
nums[1] = 7

2 + 7 = 9

Therefore, return [0, 1].

----------------------------------------------------

Example 3:
Input:
nums = [1, 2, 4, 8, 10]
target = 20

Output:
[]

Explanation:
No two numbers in the array have a sum equal to 20.

----------------------------------------------------

Approach: Two Pointers

Because the array is sorted:

- Use `left` pointer at the beginning.
- Use `right` pointer at the end.
- Calculate their sum.

If sum == target:
    We found the answer.

If sum > target:
    Move `right` left to get a smaller number.

If sum < target:
    Move `left` right to get a larger number.
"""

from typing import List


class Solution:
    def twoSumSortedArray(self, nums: List[int], target: int) -> List[int]:

        # 'left' pointer starts from the first element.
        left = 0

        # 'right' pointer starts from the last element.
        right = len(nums) - 1

        # Continue until both pointers meet.
        # This also prevents using the same element twice.
        while left < right:

            # Calculate the sum of the numbers
            # at the left and right pointers.
            current_sum = nums[left] + nums[right]

            # If the sum matches the target,
            # return the indexes.
            if current_sum == target:
                return [left, right]

            # If the sum is greater than the target,
            # move the right pointer left.
            #
            # Since the array is sorted, moving left
            # gives us a smaller number.
            elif current_sum > target:
                right -= 1

            # If the sum is smaller than the target,
            # move the left pointer right.
            #
            # Since the array is sorted, moving right
            # gives us a larger number.
            else:
                left += 1

        # Return an empty list if no pair is found.
        return []


obj = Solution()

print(obj.twoSumSortedArray([2, 3, 8, 11, 20, 35, 52], 23))
# Output: [1, 4]