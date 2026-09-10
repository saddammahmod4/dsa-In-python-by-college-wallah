from typing import List

class Solution:
    def maxWealth(self, accounts: List[List[int]]) -> int:
        output = 0

        for account in accounts:
            output = max(output, sum(account))

        return output

obj = Solution()
print(obj.maxWealth([[1,2,3], [3,2,1]]))