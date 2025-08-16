class Solution:
    def maximum69Number (self, num: int) -> int:
        str_num = str(num)

        for idx in range(len(str_num)):
            if str_num[idx] == '6':
                return int(str_num[:idx] + '9' + str_num[idx + 1:])
        return num