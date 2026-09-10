"""
Question:
Given a string `text`, determine whether it is a palindrome.

A palindrome is a word or string that reads the same from left to right
and right to left.

Use the two-pointer approach:
- `i` starts from the beginning.
- `j` starts from the end.
- Compare both characters.
- Move both pointers toward the center.

Example 1:
Input:
text = "racecar"

Output:
True

Explanation:
r a c e c a r
^           ^
i           j

Characters match, so move inward.

r a c e c a r
  ^       ^
  i       j

Continue until the middle.
The string is a palindrome.

----------------------------------------------------

Example 2:
Input:
text = "hello"

Output:
False

Explanation:
h != o

The first and last characters are different,
so it is not a palindrome.

----------------------------------------------------

Example 3:
Input:
text = "madam"

Output:
True

Explanation:
m == m
a == a
d == d

Therefore, it is a palindrome.
"""


class Solution:
    def isPalindrome(self, text: str) -> bool:

        # 'i' points to the first character.
        i = 0

        # 'j' points to the last character.
        j = len(text) - 1

        # Continue until the two pointers meet.
        while i < j:

            # Compare characters from both ends.
            if text[i] == text[j]:

                # Characters match, so move the left pointer forward.
                i += 1

                # Move the right pointer backward.
                j -= 1

            else:
                # Characters do not match,
                # so the string is NOT a palindrome.
                return False

        # If all characters matched, it is a palindrome.
        return True


obj = Solution()

print(obj.isPalindrome("racecar"))  # True
print(obj.isPalindrome("madam"))    # True
print(obj.isPalindrome("hello"))    # False