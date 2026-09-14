"""
LeetCode 1876. Substrings of Size Three with Distinct Characters

Question:
Given a string `string`, count how many substrings of length 3
contain three distinct characters.

A substring is called "good" if:
- Its length is exactly 3.
- All three characters are different.

Example 1:
Input:
string = "xyzzaz"

Output:
1

Explanation:

Check every substring of length 3:

"xyz" → x, y, z are all different → Good
"yzz" → z appears twice → Not Good
"zza" → z appears twice → Not Good
"zaz" → z appears twice → Not Good

Therefore, the total number of good substrings is 1.

----------------------------------------------------

Example 2:
Input:
string = "aababcabc"

Output:
4

Explanation:

Substrings of length 3:

"aab" → a appears twice → Not Good
"aba" → a appears twice → Not Good
"bab" → b appears twice → Not Good
"abc" → a, b, c are all different → Good
"bca" → b, c, a are all different → Good
"cab" → c, a, b are all different → Good
"abc" → a, b, c are all different → Good

Therefore, the total number of good substrings is 4.
"""


class Solution:
    def countGoodSubString(self, string: str) -> int:

        # Store the total number of good substrings found.
        count = 0

        # Store the length of the string.
        n = len(string)

        # Go through every possible starting position
        # for a substring of length 3.
        #
        # We use n - 2 because we need:
        # string[i], string[i + 1], and string[i + 2].
        for i in range(n - 2):

            # Check whether all three characters are different.
            #
            # Example:
            # "abc"
            #
            # a != b → True
            # b != c → True
            # c != a → True
            #
            # Therefore, "abc" is a good substring.
            if (
                string[i] != string[i + 1]
                and string[i + 1] != string[i + 2]
                and string[i + 2] != string[i]
            ):

                # Increase the count because we found
                # a good substring.
                count += 1

        # Return the total number of good substrings.
        return count


obj = Solution()

print(obj.countGoodSubString("xyzzaz"))      # Output: 1
print(obj.countGoodSubString("aababcabc"))   # Output: 4