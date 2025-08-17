class Solution:
    def isValid(self, s: str) -> bool:
        staples = {
            '}': '{',
            ')': '(',
            ']': '['
        }

        queue = []
        for staple in s:
            if staple in '})]':
                if not queue or queue[-1] != staples[staple]:
                    return False
                queue.pop()
            else:
                queue.append(staple)

        return not queue