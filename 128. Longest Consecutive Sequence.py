class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0

        set_nums = set(nums)
        max_length = 0

        for num in set_nums:
            num_lower = num - 1

            if num_lower not in set_nums:
                count = 0

                while num in set_nums:
                    count += 1
                    num += 1
                
                max_length = max(max_length, count)
        
        return max_length