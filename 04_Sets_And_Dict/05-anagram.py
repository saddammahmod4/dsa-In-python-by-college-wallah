"""
LeetCode 242. Valid Anagram

Question:
Given two strings `str1` and `str2`, determine whether `str2`
is an anagram of `str1`.

An anagram is a word or phrase formed by rearranging the characters
of another word, using all characters exactly the same number of times.

Return:
- True  -> If both strings are anagrams.
- False -> If both strings are not anagrams.

Example 1:
Input:
str1 = "anagram"
str2 = "nagaram"

Output:
True

Explanation:
Both strings contain the same characters with the same frequency.

anagram:
a -> 3
n -> 1
g -> 1
r -> 1
m -> 1

nagaram:
n -> 1
a -> 3
g -> 1
r -> 1
m -> 1

Therefore, they are anagrams.

----------------------------------------------------

Example 2:
Input:
str1 = "rat"
str2 = "car"

Output:
False

Explanation:
str1 contains:
r -> 1
a -> 1
t -> 1

str2 contains:
c -> 1
a -> 1
r -> 1

The characters are different, so they are not anagrams.

----------------------------------------------------

Example 3:
Input:
str1 = "listen"
str2 = "silent"

Output:
True

Explanation:
Both strings contain exactly the same characters:
l, i, s, t, e, n

Only their order is different.
"""


class Solution:
    def isAnagram(self, str1: str, str2: str) -> bool:

        # If the lengths are different, they cannot be anagrams.
        #
        # Example:
        # "cat" has length 3
        # "cats" has length 4
        #
        # Therefore, they cannot contain the same characters.
        if len(str1) != len(str2):
            return False

        # Create an empty dictionary to store
        # the frequency (count) of each character.
        freq = {}

        # Count the frequency of every character in str1.
        for char in str1:

            # If the character is not already in the dictionary,
            # add it with an initial count of 1.
            if char not in freq:
                freq[char] = 1

            # Otherwise, increase its count by 1.
            else:
                freq[char] += 1

        # Go through every character in str2.
        for char in str2:

            # If a character from str2 does not exist in str1,
            # the strings cannot be anagrams.
            if char not in freq:
                return False

            # Decrease the frequency because we found
            # the same character in str2.
            else:
                freq[char] -= 1

        # Check every remaining frequency value.
        for count in freq.values():

            # If any count is not 0, the character frequencies
            # in both strings are different.
            if count != 0:
                return False

        # All characters have the same frequency.
        # Therefore, the strings are anagrams.
        return True


obj = Solution()

print(obj.isAnagram("anagram", "nagaram"))  # Output: True
print(obj.isAnagram("rat", "car"))          # Output: False
