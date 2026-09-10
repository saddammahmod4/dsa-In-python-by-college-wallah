"""
LeetCode 1. Two Sum

Question:
Given an array of integers `numbers` and an integer `target`,
return the indexes of the two numbers whose sum is equal to `target`.

Rules:
- Each input element can be used only once.
- Return the indexes of the two numbers.
- The order of the indexes does not matter.

Example 1:
Input:
numbers = [2, 7, 11, 15]
target = 9

Output:
[0, 1]

Explanation:
numbers[0] = 2
numbers[1] = 7

2 + 7 = 9

Therefore, return [0, 1].

----------------------------------------------------

Example 2:
Input:
numbers = [2, 7, 11, 15]
target = 26

Output:
[2, 3]

Explanation:
numbers[2] = 11
numbers[3] = 15

11 + 15 = 26

Therefore, return [2, 3].

====================================================
APPROACH 1: BRUTE FORCE USING NESTED LOOPS
====================================================

Check every possible pair of numbers.

Time Complexity: O(n²)
Space Complexity: O(1)

====================================================
APPROACH 2: OPTIMIZED USING A DICTIONARY
====================================================

For every number, calculate the number needed to
reach the target and check whether it was already seen.

Formula:

needed = target - current_number

Time Complexity: O(n)
Space Complexity: O(n)
"""


from typing import List


# ====================================================
# APPROACH 1: BRUTE FORCE USING NESTED LOOPS
# ====================================================
class Solution:

    def twoSumUsingArr(self, numbers: List[int], target: int) -> List[int]:

        # Loop through every number in the array.
        for i in range(len(numbers)):

            # Start from i + 1.
            # This prevents using the same element twice.
            for j in range(i + 1, len(numbers)):

                # Check whether the current pair adds up to the target.
                if numbers[i] + numbers[j] == target:

                    # Return the indexes of the two numbers.
                    return [i, j]

        # Return an empty list if no valid pair is found.
        return []


obj = Solution()

print(obj.twoSumUsingArr([2, 7, 11, 15], 26))

# Output: [2, 3]


# ====================================================
# APPROACH 2: OPTIMIZED USING A DICTIONARY
# ====================================================
class Solution:

    def twoSumUsingDict(self, numbers: List[int], target: int) -> List[int]:

        n = len(numbers)

        # Create an empty dictionary. It will store number -> index
        seen = {}

        # Loop through every number.
        for i in range(n):

            # Calculate the number needed to reach the target.
            needed = target - numbers[i]

            # Check whether the needed number. Already exists in the dictionary.
            if needed in seen:

                # Return: Index of the previously seen number and index of the current number.
                return [seen[needed], i]

            # Store the current number and its index.
            # {11: 2}
            seen[numbers[i]] = i

        # Return an empty list if no valid pair is found.
        return []

obj = Solution()

print(obj.twoSumUsingDict([2, 7, 11, 15], 26))

# Output: [2, 3]
