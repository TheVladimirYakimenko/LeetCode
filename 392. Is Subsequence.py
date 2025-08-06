class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        if not s:
            return True
        elif not t:
            return False
        
        idx_2 = -1

        for idx_1 in range(len(s)):
            for idx_2 in range(idx_2 + 1, len(t)):
                if s[idx_1] == t[idx_2]:
                    break
            else:
                return False
        
        return idx_1 == len(s) - 1
