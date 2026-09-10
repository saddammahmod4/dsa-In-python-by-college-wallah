"""
Question:
Given a string `statement` containing words separated by spaces,
reverse the order of the words and return the resulting string.

The words themselves should remain unchanged.

Example 1:
Input:
statement = "The sky is blue"

Output:
"blue is sky The"

Explanation:
Original words:
["The", "sky", "is", "blue"]

Reverse the order:
["blue", "is", "sky", "The"]

Join them with spaces:
"blue is sky The"

----------------------------------------------------

Example 2:
Input:
statement = "Hello World"

Output:
"World Hello"

----------------------------------------------------

Example 3:
Input:
statement = "I love Python"

Output:
"Python love I"
"""


class Solution:
    def reverseWords(self, statement: str) -> str:

        # Split the sentence into individual words.
        # Example:
        # "The sky is blue"
        # becomes:
        # ["The", "sky", "is", "blue"]
        split_statement = statement.split(" ")

        # Store the number of words.
        n = len(split_statement)

        # Create an empty list to store words in reverse order.
        output = []

        # Start from the last index and move toward the first index.
        #
        # range(n, 0, -1) for n = 4 gives:
        # 4, 3, 2, 1
        for i in range(n, 0, -1):

            # Python list indexes start from 0,
            # so use i - 1 to access the correct index.
            #
            # i = 4 → split_statement[3] → "blue"
            # i = 3 → split_statement[2] → "is"
            # i = 2 → split_statement[1] → "sky"
            # i = 1 → split_statement[0] → "The"
            output.append(split_statement[i - 1])

        # Join all reversed words with a space.
        return " ".join(output)


obj = Solution()

print(obj.reverseWords("The sky is blue"))
# Output: "blue is sky The"