class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        stack_length = 0
        bracket_map = {
            ')': '(',
            '}': '{',
            ']': '['
        }
        for c in s:
            if c in ['(', '{', '[']:
                stack.append(c)
                stack_length += 1
            elif stack_length == 0 or stack.pop() != bracket_map[c]:
                return False
            else:
                stack_length -= 1
        if stack_length != 0:
            return False
        return True

        