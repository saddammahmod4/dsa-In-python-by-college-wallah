"""
Question:
Given a string `text`, return the string reversed.

Example 1:
Input:
text = "hello"

Output:
"olleh"

Explanation:
Original:  h e l l o
Reverse:   o l l e h

----------------------------------------------------

Example 2:
Input:
text = "text"

Output:
"txet"

Explanation:
Original:  t e x t
Reverse:   t x e t

----------------------------------------------------

Example 3:
Input:
text = "Python"

Output:
"nohtyP"
"""

class Solution:

    def reverseString(self, text: str) -> str:

        # [::-1] is Python slicing syntax used to reverse a string.
        #
        # Start = not specified → start from the beginning
        # Stop  = not specified → go until the end
        # Step  = -1 → move from right to left
        return text[::-1]


obj = Solution()

print(obj.reverseString("text"))
# Output: "txet"