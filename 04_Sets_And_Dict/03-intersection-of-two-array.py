"""
LeetCode 349. Intersection of Two Arrays

Question:
Given two integer arrays `nums1` and `nums2`, return an array
containing their intersection.

The intersection contains only the elements that appear in BOTH arrays.

Important:
- Each element in the result should be unique.
- Duplicate values should appear only once in the result.
- The order of the result does not matter.

Example 1:
Input:
nums1 = [1, 2, 2, 1]
nums2 = [2, 2]

Output:
[2]

Explanation:
The number 2 appears in both arrays.

Even though 2 appears multiple times, the result should contain
only one 2 because the intersection requires unique elements.

----------------------------------------------------

Example 2:
Input:
nums1 = [4, 9, 5]
nums2 = [9, 4, 9, 8, 4]

Output:
[9, 4]

Explanation:
Common elements are:
4 and 9

The order can also be:
[4, 9]

because the order of the result does not matter.

----------------------------------------------------

Approach:

1. Convert both arrays into sets.
2. Sets automatically remove duplicate values.
3. Use the `&` operator to find common elements.
4. Convert the result back into a list.

Example:

set([1, 2, 2, 1])
becomes:
{1, 2}

set([2, 2])
becomes:
{2}

{1, 2} & {2}
becomes:
{2}
"""

from typing import List


class Solution:

    def intersectionOfTwoArray(
        self,
        nums1: List[int],
        nums2: List[int]
    ) -> List[int]:

        # Convert nums1 into a set.
        # This automatically removes duplicate values.
        #
        # [1, 2, 2, 1] → {1, 2}
        set1 = set(nums1)

        # Convert nums2 into a set.
        # This also removes duplicate values.
        #
        # [2, 2] → {2}
        set2 = set(nums2)

        # Find common elements using the & operator.
        #
        # {1, 2} & {2} → {2}
        intersection = set1 & set2

        # Convert the set back into a list and return it.
        return list(intersection)


obj = Solution()

print(obj.intersectionOfTwoArray([1, 2, 2, 1], [2, 2]))

# Output: [2]