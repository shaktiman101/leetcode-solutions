class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for op in s:
            if op in ['(', '{', '[']:
                stack.append(op)
            elif len(stack) == 0:
                return False
            elif op==')' and stack[-1]=='(':
                stack.pop()
            elif op=='}' and stack[-1]=='{':
                stack.pop()
            elif op==']' and stack[-1]=='[':
                stack.pop()
            else:
                return False
        
        if len(stack) != 0:
            return False
        return True
