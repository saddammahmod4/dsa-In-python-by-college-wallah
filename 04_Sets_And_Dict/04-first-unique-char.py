"""
LeetCode 387. First Unique Character in a String

Question:
Given a string `word`, return the index of the first character
that does not repeat anywhere else in the string.

If every character appears more than once, return -1.

Example 1:
Input:
word = "leetcode"

Output:
0

Explanation:
Character frequencies:
l -> 1
e -> 3
t -> 1
c -> 1
o -> 1
d -> 1

The first character with frequency 1 is "l".

Index of "l" = 0

Therefore, return 0.

----------------------------------------------------

Example 2:
Input:
word = "loveleetcode"

Output:
2

Explanation:
Character frequencies include:
l -> 2
o -> 2
v -> 1
e -> 4
...

Starting from the beginning:
l -> repeated
o -> repeated
v -> appears only once

The first unique character is "v".

Index of "v" = 2

Therefore, return 2.

----------------------------------------------------

Example 3:
Input:
word = "aabb"

Output:
-1

Explanation:
a -> appears 2 times
b -> appears 2 times

There is no character that appears exactly once.

Therefore, return -1.
"""


class Solution:
    def firstUniqueChar(self, word: str) -> int:

        # Create an empty dictionary to store
        # the frequency of each character.
        freq = {}

        # Go through every character in the word.
        for char in word:

            # If the character is not in the dictionary,
            # add it with a count of 1.
            if char not in freq:
                freq[char] = 1

            # If the character already exists,
            # increase its frequency by 1.
            else:
                freq[char] += 1

        # Go through the word again from left to right
        # to find the FIRST character with frequency 1.
        for i in range(len(word)):

            # Check whether the current character appears
            # exactly one time in the entire word.
            if freq[word[i]] == 1:

                # Return the index of the first unique character.
                return i

        # If no character has frequency 1,
        # return -1.
        return -1


obj = Solution()

print(obj.firstUniqueChar("leetcode"))      # Output: 0
print(obj.firstUniqueChar("loveleetcode"))  # Output: 2
print(obj.firstUniqueChar("aabb"))          # Output: -1