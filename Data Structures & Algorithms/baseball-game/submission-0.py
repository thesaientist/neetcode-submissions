class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        # i = 0
        # ele_n = None
        # ele_nm1 = None
        for op in operations:
            if op == "+":
                # record[i] = ele_n + ele_nm1
                record.append(record[-1] + record[-2])
            elif op == "D":
                record.append(2 * record[-1])
            elif op == "C":
                record.pop()
                # ele_n = ele_nm1
                # ele_nm1 = record[-2]
            else:
                # ele_nm1 = ele
                # ele_n = op
                record.append(int(op))
            # i += 1
        return sum(record)
