class Solution:
    def countBits(self, n: int) -> List[int]:
        result = [0] * (n + 1)
        
        for num in range(1, n + 1):
            result[num] = result[num // 2] + num % 2
        
        return result