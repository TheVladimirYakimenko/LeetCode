class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        idx = -1
        digits[idx], overflow = (digits[idx] + 1) % 10, (digits[idx] + 1) // 10
        
        while abs(idx) < len(digits) and overflow:
            idx -= 1
            digits[idx], overflow = (digits[idx] + overflow) % 10, (digits[idx] + overflow) // 10
        
        return [1] + digits if overflow else digits
