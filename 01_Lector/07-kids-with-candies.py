"""
LeetCode 1431. Kids With the Greatest Number of Candies

Question:
There are `n` kids, and each kid has a certain number of candies.

You are given:
- An integer array `candies`, where `candies[i]` represents the number of
  candies the i-th kid has.
- An integer `extraCandies`, representing the number of extra candies
  that can be given to each kid.

For each kid, determine whether giving all the extra candies to that kid
would make them have the greatest number of candies among all kids.

Return a list of boolean values where:
- True  -> The kid can have the greatest number of candies.
- False -> The kid cannot have the greatest number of candies.

Example:

Input:
candies = [2, 3, 5, 1, 3]
extraCandies = 3

Output:
[True, True, True, False, True]

Explanation:
Maximum candies any kid currently has = 5

Kid 1: 2 + 3 = 5  -> True
Kid 2: 3 + 3 = 6  -> True
Kid 3: 5 + 3 = 8  -> True
Kid 4: 1 + 3 = 4  -> False
Kid 5: 3 + 3 = 6  -> True
"""

from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        max_candies = max(candies)
        output = []

        for i in candies:
            if (i + extraCandies) >= max_candies:
                output.append(True)
            else:
                output.append(False)

        return output

obj = Solution()
print(obj.kidsWithCandies([2, 3, 5, 1, 3], 3))