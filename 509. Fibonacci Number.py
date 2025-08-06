class Solution:
    def fib(self, n: int) -> int:
        if n == 0:
            return 0

        num_1 = 0
        num_2 = 1
        
        for _ in range(n - 1):
            num_1, num_2 = num_2, num_1 + num_2
        
        return num_2