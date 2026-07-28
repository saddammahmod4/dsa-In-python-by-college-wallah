"""
Question:
Given an integer `number`, return the nth Fibonacci number.

The Fibonacci sequence is a series of numbers where:
- The first number is 0.
- The second number is 1.
- Every next number is the sum of the previous two numbers.

Formula:
F(0) = 0
F(1) = 1
F(n) = F(n-1) + F(n-2), for n >= 2

Example 1:
Input:  number = 2
Output: 1

Explanation:
Fibonacci sequence: 0, 1, 1
The 2nd Fibonacci number is 1.

Example 2:
Input:  number = 4
Output: 3

Explanation:
Fibonacci sequence: 0, 1, 1, 2, 3
The 4th Fibonacci number is 3.

Example 3:
Input:  number = 6
Output: 8

Explanation:
Fibonacci sequence: 0, 1, 1, 2, 3, 5, 8
The 6th Fibonacci number is 8.
"""

class Solution:
    def fibonacciNumber(self, number: int) -> int:

        # Base case:
        # If the number is 0 or 1, return it directly.
        if number == 0 or number == 1:
            return number

        # Recursive case:
        # Fibonacci(n) = Fibonacci(n-1) + Fibonacci(n-2)
        return self.fibonacciNumber(number - 1) + self.fibonacciNumber(number - 2)


obj = Solution()
print(obj.fibonacciNumber(6))  # Output: 8