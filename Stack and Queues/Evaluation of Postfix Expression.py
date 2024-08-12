class Solution:
    
    #Function to evaluate a postfix expression.
    def evaluatePostfix(self, S):
        stack = []
        for c in S:
            if c == '+':
                stack.append(stack.pop() + stack.pop())
            elif c == '*':
                stack.append(stack.pop() * stack.pop())
            elif c == '-':
                b = stack.pop()
                stack.append(stack.pop() - b)
            elif c == '/':
                b = stack.pop()
                stack.append(stack.pop() // b)
            else:
                stack.append(ord(c) - ord('0'))
        return stack.pop()