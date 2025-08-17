class Solution:
    def isValid(self, s: str) -> bool:
        staples = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        stack = []
        for staple in s:
            if staple in '})]':
                if not stack or stack[-1] != staples[staple]:
                    return False
                stack.pop()
            else:
                stack.append(staple)

        return not stack