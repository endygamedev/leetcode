# Link: https://leetcode.com/problems/evaluate-reverse-polish-notation

# Time Complexity: O(n)
# Space Complexity: O(1)


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for token in tokens:
            if token == "+":
                stack.append(stack.pop() + stack.pop())
            elif token == "-":
                x, y = stack.pop(), stack.pop()
                stack.append(y - x)
            elif token == "*":
                stack.append(stack.pop() * stack.pop())
            elif token == "/":
                x, y = stack.pop(), stack.pop()
                stack.append(int(y / x))
            else:
                stack.append(int(token))

        return stack.pop()
