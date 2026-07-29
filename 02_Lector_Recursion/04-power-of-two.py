class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        while n % 2 == 0:
            n //= 2

        return n == 1

    def isPowerOfTwoWithRecursion(self, n: int) -> bool:
        # base case
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 2 != 0:
            return False

        # recursive case
        return self.isPowerOfTwoWithRecursion(n // 2)

obj = Solution()
print(obj.isPowerOfTwo(16))
print(obj.isPowerOfTwo(6))
print(obj.isPowerOfTwoWithRecursion(16))
print(obj.isPowerOfTwoWithRecursion(6))