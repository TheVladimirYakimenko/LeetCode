class Solution:
    def isPalindrome(self, s: str) -> bool:
        left = 0
        right = len(s) - 1
        valid_chars = set('abcdefghijklmnopqrstuvwxyz0123456789')
        string = s.lower()

        while left < right:
            if string[left] not in valid_chars:
                left += 1
            elif string[right] not in valid_chars:
                right -= 1
            elif string[left] != string[right]:
                return False
            else:
                left += 1
                right -= 1
        
        return True