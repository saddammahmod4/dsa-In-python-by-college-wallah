from typing import List

class Solution:
    def intersectionOfTwoArray(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return list(set(nums1)&set(nums2))

obj = Solution()
print(obj.intersectionOfTwoArray([1, 2, 2, 1], [2, 2]))