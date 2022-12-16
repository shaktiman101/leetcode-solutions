from collections import deque
class MyQueue:

    def __init__(self):
        self.stack1 = []
        self.stack2 = []
    def push(self, x: int) -> None:
        self.stack1.append(x)

    def pop(self) -> int:
        n = len(self.stack1)
        while n > 1:
            ele = self.stack1.pop()
            n -= 1
            self.stack2.append(ele)
        ans = self.stack1.pop()
        
        n = len(self.stack2)
        while n > 0:
            ele = self.stack2.pop()
            n -= 1
            self.stack1.append(ele)
        return ans

    def peek(self) -> int:
        return self.stack1[0]

    def empty(self) -> bool:
        if self.stack1:
            return False
        return True
        


# Your MyQueue object will be instantiated and called as such:
# obj = MyQueue()
# obj.push(x)
# param_2 = obj.pop()
# param_3 = obj.peek()
# param_4 = obj.empty()