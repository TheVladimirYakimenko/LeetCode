class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for idx in range(len(haystack) - len(needle) + 1):
            try:
                if haystack[idx : idx + len(needle)] == needle:
                    return idx
            except IndexError:
                return -1
        return -1