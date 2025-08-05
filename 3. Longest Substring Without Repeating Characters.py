class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_length = 0
        temp_length = 0
        new_begin = 0

        for idx in range(len(s)):
            try:
                new_begin = s.index(s[idx], new_begin, idx) + 1
            except ValueError:
                temp_length += 1
            else:
                if max_length < temp_length:
                    max_length = temp_length
                temp_length = idx - new_begin + 1
                
            if len(s) - idx <= max_length - temp_length:
                return max_length
            
        return max(max_length, temp_length)