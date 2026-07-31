class Solution:
    def calPoints(self, operations: List[str]) -> int:
        stack: list[str] = []
        for op in operations:
            if op == 'C':
                if stack:
                    stack.pop()
            elif op == 'D':
                stack.append(int(stack[-1]) * 2)
            elif op == '+':
                num1 = int(stack.pop())
                num2 = int(stack.pop())
                stack.append(str(num2))
                stack.append(str(num1))
                stack.append(str(num1 + num2))
            else:
                stack.append(op)

        sum = 0
        while stack:
            sum += int(stack.pop())
        return sum
