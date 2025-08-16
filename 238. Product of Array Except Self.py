class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        mult = 1
        has_zero = False

        for num in nums:
            if num or has_zero:
                mult *= num
            else:
                has_zero = True

        if has_zero:
            return [0 if number else mult for number in nums]        
        return [mult // number for number in nums]
