class Solution:
    def firstUniqueChar(self, word: str) -> int:

        freq = {}
        for i in word:
            if i not in freq:
                freq[i] = 1
            else:
                freq[i] += 1

        for i in range(len(word)):
            if freq[word[i]] == 1:
                return i

        return -1

obj = Solution()
print(obj.firstUniqueChar("leetcode"))
print(obj.firstUniqueChar("loveleetcode"))
print(obj.firstUniqueChar("aabb"))