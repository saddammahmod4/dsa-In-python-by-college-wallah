"""
LeetCode 58. Length of Last Word

Question:
Given a string `statement` consisting of words and spaces,
return the length of the last word in the string.

A word is a maximal sequence of non-space characters.

Example 1:
Input:
statement = "Hello World"

Output:
5

Explanation:
The last word is "World".
Length of "World" = 5

----------------------------------------------------

Example 2:
Input:
statement = "Fly me to the moon "

Output:
4

Explanation:
The trailing space is removed.

Words:
["Fly", "me", "to", "the", "moon"]

The last word is "moon".
Length of "moon" = 4

----------------------------------------------------

Example 3:
Input:
statement = "luffy is still joyboy"

Output:
6

Explanation:
The last word is "joyboy".
Length of "joyboy" = 6
"""


class Solution:
    def lengthOfLastWord(self, statement: str) -> int:

        # Remove spaces from the beginning and end of the string.
        #
        # "Fly me to the moon "
        # becomes:
        # "Fly me to the moon"
        strip_statement = statement.strip()

        # Split the string into individual words.
        #
        # "Fly me to the moon"
        # becomes:
        # ["Fly", "me", "to", "the", "moon"]
        split_statement = strip_statement.split(" ")

        # Reverse the list of words.
        #
        # ["Fly", "me", "to", "the", "moon"]
        # becomes:
        # ["moon", "the", "to", "me", "Fly"]
        reverse_statement = split_statement[::-1]

        # The first element is now the last word.
        # Return the length of that word.
        #
        # "moon" → 4
        return len(reverse_statement[0])


obj = Solution()

print(obj.lengthOfLastWord("Fly me to the moon "))
# Output: 4