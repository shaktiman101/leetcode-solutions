class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        n = len(position)
        cars = sorted(zip(position, speed), reverse=True)
        time_taken = []

        for pos, s in cars:
            t = (target - pos)/s
            time_taken.append(t)

        stack = []
        for idx, time in enumerate(time_taken):
            while not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)