class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        n = len(tokens)
        stack = []
        for i in range(n):
            if tokens[i] not in ['+','*','-','/']:
                stack.append(int(tokens[i]))
            else:
                op1 = stack.pop()
                op2 = stack.pop()
                if tokens[i] == '+':
                    stack.append(op1+op2)
                elif tokens[i] == '-':
                    stack.append(op2-op1)
                elif tokens[i] == '*':
                    stack.append(op1*op2)
                else:
                    stack.append(int(op2/op1))

        return stack[0]