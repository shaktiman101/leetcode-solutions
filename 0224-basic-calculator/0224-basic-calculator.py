import re
class Solution:
    def calculate(self, s: str) -> int:
        res, num, sign, stack = 0, 0, 1, []
        for ss in s:
            if ss.isdigit():
                num = 10*num + int(ss)
            elif ss in ["-", "+"]:
                res += sign*num
                num = 0
                sign = [-1, 1][ss=="+"]
            elif ss == "(":
                stack.append(res)
                stack.append(sign)
                sign, res = 1, 0
            elif ss == ")":
                res += sign*num
                res *= stack.pop()
                res += stack.pop()
                num = 0
        return res + num*sign
    
        exp = re.split('(\d+)', s)
        stack = []
        for ch in exp:
            ch = ch.strip()
            if ch.isdigit():
                if stack and stack[-1] != '(':
                    op = stack.pop()
                    num2 = int(ch)
                    if stack:
                        num1 = stack.pop()

                        if op == '+':
                            stack.append(num1 + num2)
                        elif op == '-':
                            stack.append(num1 - num2)
                    else:
                        stack.append(-num2)
                else:                
                    stack.append(int(ch))
            elif ch == ')':
                num2 = stack.pop()
                op_bracket = stack.pop()
                if op_bracket == '-':
                    stack.pop() # pop opening bracket
                    if stack:
                        op = stack.pop()
                        num1 = stack.pop()
                        if op == '+':
                            stack.append(num1 - num2)
                        elif op == '-':
                            stack.append(num1 + num2)
                    else:
                        stack.append(-num2)
                elif stack:
                    op = stack.pop()
                    num1 = stack.pop()
                    if op == '+':
                        stack.append(num1 + num2)
                    elif op == '-':
                        stack.append(num1 - num2)
                else:
                    stack.append(num2)
            elif ch == '+' or ch == '-' or ch == '(':
                stack.append(ch)

        return stack[-1]
