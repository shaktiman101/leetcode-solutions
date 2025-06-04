class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        ans = []

        def is_valid(paran):
            stack = []
            for op in paran:
                if op == '(':
                    stack.append(op)
                else:
                    if not stack or stack[-1] == ')':
                        return False
                    stack.pop()
            return True
        
        left, right = n, n

        def form_paran(left, right, tmp):
            # if left < 0 or right < 0:
            #     return

            if left == 0 and right == 0:
                if is_valid(tmp):
                    return ans.append("".join(tmp.copy()))
            
            if left > 0:
                tmp.append("(")
                form_paran(left-1, right, tmp)
                tmp.pop()

            if right > left:
                tmp.append(")")
                form_paran(left, right-1, tmp)
                tmp.pop()


        form_paran(n, n, [])
        return ans

        

