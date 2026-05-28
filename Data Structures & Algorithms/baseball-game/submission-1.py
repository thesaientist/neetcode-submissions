class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        points = 0
        for op in operations:
            if op == "+":
                points += record[-1] + record[-2]
                record.append(record[-1] + record[-2])
            elif op == "D":
                points += 2 * record[-1]
                record.append(2 * record[-1])
            elif op == "C":
                popped_ele = record.pop()
                points -= popped_ele
            else:
                points += int(op)
                record.append(int(op))
        return sum(record)
