class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        letters_dict_1 = {}
        letters_dict_2 = {}

        for idx in range(len(s)):
            letter_1 = s[idx]
            letter_2 = t[idx]

            letters_dict_1[letter_1] = letters_dict_1.get(letter_1, 0) + 1
            letters_dict_2[letter_2] = letters_dict_2.get(letter_2, 0) + 1

        return letters_dict_1 == letters_dict_2