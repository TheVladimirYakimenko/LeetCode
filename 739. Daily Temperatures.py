class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack = []
        result = [0 for _ in temperatures]

        for idx in range(len(temperatures)):
            cur_temp = temperatures[idx]

            while stack and cur_temp > temperatures[stack[-1]]:
                prev_idx = stack.pop()
                result[prev_idx] = idx - prev_idx
            
            stack.append(idx)

        return result