class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        power = 0

        while 4 ** power <= n:
            if 4 ** power == n:
                return True
            power += 1
        return False