class MinStack:

    def __init__(self):
        self.stack = []
        self.min_vals = []
        self.min_val_count = {}
        
    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.min_vals or val < self.min_vals[-1]:
            self.min_vals.append(val)
            if val in self.min_val_count:
                self.min_val_count[val] += 1
            else:
                self.min_val_count[val] = 1
        elif val == self.min_vals[-1]:
            self.min_val_count[val] += 1

    def pop(self) -> None:
        removed_val = self.stack.pop()
        if removed_val == self.min_vals[-1]:
            self.min_val_count[removed_val] -= 1
            if not self.min_val_count[removed_val]:
                self.min_vals.pop()

    def top(self) -> int:
        return self.stack[-1]
        
    def getMin(self) -> int:
        return self.min_vals[-1]
        
