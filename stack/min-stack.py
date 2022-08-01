# Link: https://leetcode.com/problems/min-stack

# push:
# Time Complexity: O(1)
# Space Complexity: O(1)

# pop:
# Time Complexity: O(1)
# Space Complexity: O(1)

# top:
# Time Complexity: O(1)
# Space Complexity: O(1)

# getMin:
# Time Complexity: O(1)
# Space Complexity: O(1)


class MinStack:

    def __init__(self):
        self.stack = []
        self.min_stack = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        minval = min(val, self.min_stack[-1] if self.min_stack else val)
        self.min_stack.append(minval)


    def pop(self) -> None:
        self.stack.pop()
        self.min_stack.pop()


    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
