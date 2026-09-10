"""
LeetCode 1108. Defanging an IP Address

Question:
Given a valid IPv4 address, replace every "." with "[.]".

Return the defanged IP address.

Example 1:
Input:
address = "1.1.1.1"

Output:
"1[.]1[.]1[.]1"

Explanation:
Every "." is replaced with "[.]".

Example 2:
Input:
address = "255.100.50.0"

Output:
"255[.]100[.]50[.]0"
"""

class Solution:
    def defangAddr(self, address: str) -> str:

        # Create an empty string to store the result.
        output = ""

        # Go through every character in the IP address.
        for i in address:

            # If the current character is NOT a dot,
            # add the character as it is.
            if i != ".":
                output += i

            # If the current character is a dot,
            # replace it with "[.]".
            else:
                output += "[.]"

        # Return the defanged IP address.
        return output


obj = Solution()

print(obj.defangAddr("1.1.1.1"))
# Output: 1[.]1[.]1[.]1