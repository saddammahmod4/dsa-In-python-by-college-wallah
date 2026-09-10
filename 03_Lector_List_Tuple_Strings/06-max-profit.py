"""
LeetCode 121. Best Time to Buy and Sell Stock

Question:
Given an array `prices` where `prices[i]` represents the price of a stock
on the i-th day, find the maximum profit you can achieve by buying on
one day and selling on a later day.

Rules:
- You can buy only once.
- You can sell only once.
- You must buy before you sell.
- If no profit is possible, return 0.

Example 1:
Input:
prices = [7, 1, 5, 3, 6, 4]

Output:
5

Explanation:
Buy at price 1.
Sell at price 6.

Profit = 6 - 1 = 5

----------------------------------------------------

Example 2:
Input:
prices = [7, 6, 4, 3, 1]

Output:
0

Explanation:
Prices keep decreasing, so there is no profitable transaction.

Therefore, return 0.
"""

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        # Store the lowest price seen so far.
        # Initially, assume the first price is the minimum.
        min_price = prices[0]

        # Store the maximum profit found so far.
        profit = 0

        # Check every day's stock price.
        for i in range(len(prices)):

            # Calculate the profit if we buy at the lowest price
            # and sell at today's price.
            current_profit = prices[i] - min_price

            # If today's profit is greater than our previous
            # maximum profit, update the profit.
            if current_profit > profit:
                profit = current_profit

            # Keep track of the lowest price seen so far.
            min_price = min(min_price, prices[i])

        # Return the maximum profit.
        return profit


obj = Solution()

print(obj.maxProfit([7, 1, 5, 3, 6, 4]))
# Output: 5