class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers) - 1

        while left < right:
            cur_num = numbers[left] + numbers[right]
            
            if cur_num < target:
                left += 1
            elif cur_num > target:
                right -= 1
            else:
                return [left + 1, right + 1]