class Solution:
    def decodeString(self, s: str) -> str:
        def inner(idx: int):
            string = ''
            number = ''
            length = len(s)

            while idx < length:
                char = s[idx]

                if char in '0123456789':
                    number += char
                elif char == '[':
                    if not number:
                        number = '1'
                    decode_str, idx = inner(idx + 1)
                    string += int(number) * decode_str
                    number = ''
                elif char == ']':
                    return string, idx
                else:
                    string += char
                
                idx += 1
            
            return string
        
        result = inner(0)
        return result[0] if isinstance(result, tuple) else result