"""
LeetCode 49. Group Anagrams

Question:
Given an array of strings `strs`, group all strings that are anagrams
of each other.

Return the groups of anagrams.

An anagram is a word formed by rearranging the characters of another word.
Two words are anagrams if they contain the same characters with the same
frequency.

The order of the groups does not matter.

Example 1:
Input:
strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

Output:
[
    ["eat", "tea", "ate"],
    ["tan", "nat"],
    ["bat"]
]

Explanation:

"eat", "tea", and "ate" are anagrams because:

eat → aet
tea → aet
ate → aet

They all have the same sorted characters.

----------------------------------------------------

Example 2:
Input:
strs = ["tan", "nat", "bat"]

Output:
[
    ["tan", "nat"],
    ["bat"]
]

Explanation:

tan → ant
nat → ant

Therefore, "tan" and "nat" belong to the same group.

"bat" does not have another anagram in the array.

----------------------------------------------------

Approach:

1. Sort the characters of every word.
2. Use the sorted word as a dictionary key.
3. All anagrams will have the same sorted key.
4. Store words with the same key in the same list.

Example:

"eat" → sort → "aet"
"tea" → sort → "aet"
"tae" → sort → "aet"

Since all have the key "aet", they are grouped together.
"""

from typing import List


class Solution:

    def sortString(self, string: str) -> str:

        # Convert the string into a list because
        # Python can sort a list of characters.
        #
        # "eat" → ['e', 'a', 't']
        s1 = list(string)

        # Sort the characters alphabetically.
        #
        # ['e', 'a', 't'] → ['a', 'e', 't']
        s1.sort()

        # Join the sorted characters back into a string.
        #
        # ['a', 'e', 't'] → "aet"
        return "".join(s1)


    def groupAnagram(self, strs: List[str]) -> List[List[str]]:

        # Create an empty dictionary.
        #
        # Dictionary structure:
        #
        # sorted_word : list of anagrams
        #
        # Example:
        # {
        #     "aet": ["eat", "tea", "tae"],
        #     "ant": ["tan", "nat"],
        #     "abt": ["bat"]
        # }
        dict1 = {}

        # Go through every string in the input list.
        for s in strs:

            # Sort the current string to create a common key.
            #
            # "eat" → "aet"
            # "tea" → "aet"
            key = self.sortString(s)

            # If the key already exists, another anagram
            # with the same sorted characters was found.
            if key in dict1:

                # Add the current string to the existing group.
                dict1[key].append(s)

            else:

                # Create a new group for this sorted key.
                dict1[key] = [s]

        # Return only the groups of anagrams.
        # dict1.values() contains all grouped lists.
        return list(dict1.values())


obj = Solution()

print(
    obj.groupAnagram(
        ["eat", "tea", "tan", "tae", "nat", "bat"]
    )
)