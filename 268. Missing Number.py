class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        sum_nums = sum(nums)
        sum_total = (len(nums) + 1) * len(nums) // 2
        return sum_total - sum_nums