class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        op = ['+','-','*','/']
        stack = []
        
        for token in tokens:
            if token in op:
                num2 = stack.pop()
                num1 = stack.pop()
                if token == '+':
                    stack.append(num1+num2)
                elif token == '-':
                    stack.append(num1-num2)
                elif token == '*':
                    stack.append(num1*num2)
                else:
                    stack.append(int(num1/num2))
            else:
                stack.append(int(token))
        # if '.' in stack[-1]:
        #     return float(stack[-1])
        return stack[-1]