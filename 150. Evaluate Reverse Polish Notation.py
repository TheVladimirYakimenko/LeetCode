class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        def calculate(num_1, num_2, operation):
            if operation == '+':
                return num_1 + num_2
            elif operation == '-':
                return num_1 - num_2
            elif operation == '*':
                return num_1 * num_2
            else:
                return int(num_1 / num_2)
        
        stack = []
        
        for char in tokens:
            if char in '-+*/':
                num_2 = stack.pop()
                num_1 = stack.pop()
                stack.append(calculate(num_1, num_2, char))
            else:
                stack.append(int(char))
        
        return stack[-1]