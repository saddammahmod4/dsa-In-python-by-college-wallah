from typing import List

class Solution:
    def twoSumSortedArray(self, nums: List[int], target: int) -> List[int]:
        left = 0
        right = len(nums) - 1

        while left < right:
            sum1 = nums[left] + nums[right]

            if sum1 == target:
                return [left, right]

            elif sum1 > target:
                right -= 1

            else:
                left += 1

        return []

obj = Solution()
print(obj.twoSumSortedArray([2, 3, 8, 11, 20, 35, 52], 23))