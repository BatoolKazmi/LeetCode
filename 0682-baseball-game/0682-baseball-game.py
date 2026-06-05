class Solution:
    def calPoints(self, operations: List[str]) -> int:
        i = 0
        s = -1

        stack = []
        res = 0
        while i < len(operations):
            if operations[i] == "C":
                stack.pop()
                s -= 1
            elif operations[i] == "D":
                val = stack[s] * 2
                stack.append(int(val))
                s += 1
            elif operations[i] == "+":
                val = stack[s] + stack[s - 1]
                stack.append(int(val))
                s += 1
            else:
                stack.append(int(operations[i]))
                s += 1
            i += 1

        for n in stack:
            res += n

        return res 