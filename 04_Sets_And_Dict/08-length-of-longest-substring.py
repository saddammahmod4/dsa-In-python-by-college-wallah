"""
LeetCode 3. Longest Substring Without Repeating Characters

Question:
Given a string `string`, find the length of the longest substring
that contains no repeating characters.

A substring must contain consecutive characters.

Example 1:
Input:
string = "abcabcbb"

Output:
3

Explanation:
Possible substrings without repeating characters include:

"abc" → length 3
"bca" → length 3
"cab" → length 3

The longest length is 3.

----------------------------------------------------

Example 2:
Input:
string = "bbbb"

Output:
1

Explanation:
Every character is "b".

The longest substring without repeating characters is:

"b" → length 1

Therefore, return 1.

----------------------------------------------------

Example 3:
Input:
string = "pwwkew"

Output:
3

Explanation:

Possible unique substrings include:

"pw" → length 2
"wke" → length 3
"kew" → length 3

The longest substring without repeating characters has length 3.

Therefore, return 3.

----------------------------------------------------

Approach: Sliding Window

Maintain a window containing characters without duplicates.

For every new character:

1. Check whether it already exists in the current window.
2. If it exists, remove characters from the beginning
   until the duplicate is removed.
3. Add the current character to the window.
4. Update the maximum length.

Example:

string = "abcabc"

Window progression:

"a"
"ab"
"abc"
Duplicate "a" found

Remove from the beginning:
"abc" → "bc"

Add "a":
"bca"
"""


class Solution:
    def lengthOfLongestSubstring(self, string: str) -> int:

        # Store the current substring containing only unique characters.
        arr = []

        # Store the maximum length found so far.
        max_length = 0

        # Go through every character in the string.
        for char in string:

            # If the current character already exists in the window,
            # remove characters from the beginning.
            #
            # Keep removing until the duplicate character
            # no longer exists in the window.
            while char in arr:

                # Remove the first character from the current window.
                arr.pop(0)

            # Add the current character after removing duplicates.
            arr.append(char)

            # If the current window is longer than the previous
            # maximum length, update max_length.
            if len(arr) > max_length:
                max_length = len(arr)

        # Return the length of the longest substring
        # containing no repeating characters.
        return max_length


obj = Solution()

print(obj.lengthOfLongestSubstring("abcabcbb"))  # Output: 3
print(obj.lengthOfLongestSubstring("bbbb"))      # Output: 1
print(obj.lengthOfLongestSubstring("pwwkew"))    # Output: 3