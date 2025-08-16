class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dct = {}

        for string in strs:
            dct.setdefault(''.join(sorted(string)), []).append(string)

        return list(dct.values())