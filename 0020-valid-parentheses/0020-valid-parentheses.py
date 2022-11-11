class Solution:
    def isValid(self, s: str) -> bool:
        open_brackets = set(['(','{','['])
        close_brackets_map = {')':'(', '}':'{', ']':'['}
        
        stack = []
        for ch in s:
            if ch in open_brackets:
                stack.append(ch)
            else:
                if stack and close_brackets_map[ch] == stack[-1]:
                    stack.pop()
                else:
                    return False
        if stack:
            return False
        return True
        