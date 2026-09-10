from typing import List

class Solution:
    def twoSumUsingDict(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)

        dict = {}

        for i in range(n):

            needed = target - nums[i]

            if needed in dict:
                return [dict[needed], i]

            dict[nums[i]] = i

        return []

obj = Solution()
print(obj.twoSumUsingDict([2, 7, 11, 15], 22))