class Solution:
    def calPoints(self, operations: List[str]) -> int:
        score = []
        for op in operations:
            if op == '+':
                s1 = score[-1]
                s2 = score[-2]
                s = s1+s2
                score.append(s)
            elif op == 'D':
                score.append(2*score[-1])
            elif op == 'C':
                score.pop()
            else:
                score.append(int(op))

        return sum(score)