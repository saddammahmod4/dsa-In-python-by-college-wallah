"""
Question:
Print numbers from 1 to n using recursion.

Input:
n = 3

Output:
1 2 3

Explanation:
The function first goes down to the base case (n == 0).
After reaching the base case, each recursive call returns one by one,
and the numbers are printed in ascending order.
"""

def fun(n):
    # Base Case:
    # Stop the recursion when n becomes 0.
    if n == 0:
        return

    # Recursive Call:
    # Call the function with a smaller value.
    # This keeps going until n becomes 0.
    fun(n - 1)

    # This line executes AFTER the recursive call returns.
    # So the numbers are printed while coming back,
    # resulting in ascending order.
    print(n, end=" ")


# Function Call
fun(3)