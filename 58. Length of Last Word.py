class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        count = 0
        idx = -1

        while True:
            if s[idx] != ' ':
                break
            idx -= 1

        while True:
            count += 1
            
            if (count + abs(idx) - 1 >= len(s)) or (s[idx - count] == ' '):
                return count