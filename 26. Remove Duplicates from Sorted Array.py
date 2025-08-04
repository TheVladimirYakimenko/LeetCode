class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums:
            return 0

        unique_number = 1
        for temp_number in range(1, len(nums)):
            if nums[temp_number] != nums[unique_number - 1]:
                unique_number += 1
                nums[unique_number - 1] = nums[temp_number]
        
        return unique_number